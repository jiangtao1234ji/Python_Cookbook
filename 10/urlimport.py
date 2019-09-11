# @Author  :_kerman jt
# @Time    : 19-8-22 上午9:30


import sys
import importlib.abc
import imp
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from html.parser import HTMLParser
import logging

log = logging.getLogger(__name__)

def _get_links(url):
    class LinkParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag == 'a':
                attrs = dict(attrs)
                links.add(attrs.get('href').rstrip('/'))

    links = set()
    try:
        log.debug(f'Getting links from {url}')
        u = urlopen(url)
        parser = LinkParser()
        parser.feed(u.read().decode('utf-8'))
    except Exception as e:
        log.debug(f'Could not get links {e}')
    log.debug(f'links: {links}')
    return links

class UrlMetaFinder(importlib.abc.MetaPathFinder):
    def __init__(self, baseurl):
        self._baseurl = baseurl
        self._links = {}
        self._loaders = {baseurl : UrlModuleLoader(baseurl)}

    def find_module(self, fullname, path = None):
        log.debug('find_module: fullname=%r, path=%r', fullname, path)
        if path is None:
            baseurl = self._baseurl
        else:
            if not path[0].startswith(self._baseurl):
                return None
            baseurl = path[0]

        parts = fullname.split('.')
        basename = parts[-1]
        log.debug('find_module: baseurl=%r, basename=%r', baseurl, basename)
        if basename not in self._links:
            self._links[baseurl] = _get_links(baseurl)

        if basename in self._links[baseurl]:
            log.debug(f'find_module: tring package {fullname}')
            fullurl = self._baseurl + '/' + basename
            loader = UrlPackageLoader(fullurl)
            try:
                loader.load_module(fullname)
                self._links[fullurl] = _get_links(fullurl)
                self._loaders[fullurl] = UrlModuleLoader(fullurl)
                log.debug(f'find_module: packaget {fullname} loaded')
            except Exception as e:
                log.debug(f'find_module: package failed {fullname}')
                loader = None
            return loader
        filename = basename + 'py'
        if filename in self._links[baseurl]:
            log.debug(f'find_module: module {fullname} found')
            return self._loaders[baseurl]
        else:
            log.debug(f'find_module: module {fullname} not found')
            return None

    def invalidate_caches(self):
        log.debug('invalidating link cache')
        self._links.clear()

class UrlModuleLoader(importlib.abc.SourceLoader):
    def __init__(self, baseurl):
        self._baseurl = baseurl
        self._source_cache = {}

    def module_repr(self, module):
        return f'<urlmodule {module.__name__} from {module.__file__}>'

    def load_module(self, fullname):
        code = self.get_code(fullname)
        mod = sys.modules.setdefault(fullname, imp.new_module(fullname))
        mod.__file__ = self.get_filename(fullname)
        mod.__loader__ = self
        mod.__package__ = fullname.rpartition('.')[0]
        exec(code, mod.__dict__)
        return mod

    def get_code(self, fullname):
        src = self.get_code(fullname)
        return compile(src, self.get_filename(fullname), 'exec')

    def get_data(self, path):
        pass

    def get_filename(self, fullname):
        return self._baseurl + '/' + fullname.split('.')[-1] + '.py'

    def get_source(self, fullname):
        filename = self.get_filename(fullname)
        log.debug(f'loader: reading {filename}')
        if filename in self._source_cache:
            log.debug(f'loader: cached {filename}')
            return self._source_cache[filename]
        try:
            u = urlopen(filename)
            source = u.read().decode('utf-8')
            log.debug(f'loader: {filename} loaded')
            self._source_cache[filename] = source
            return source
        except (HTTPError, URLError) as e:
            log.debug(f'loader: {filename} failed {e}')
            raise ImportError(f"Can not load {filename}")

    def is_package(self, fullname):
        return False

class UrlPackageLoader(UrlModuleLoader):
    def load_module(self, fullname):
        mod = super().load_module(fullname)
        mod.__path__ = [self._baseurl]
        mod.__package__ = fullname

    def get_filename(self, fullname):
        return self._baseurl + '/' + '__init__.py'

    def is_package(self, fullname):
        return True

_installed_meta_cache = {}
def install_meta(address):
    if address not in _installed_meta_cache:
        finder = UrlMetaFinder(address)
        _installed_meta_cache[address] = finder
        sys.meta_path.append(finder)
        log.debug(f'{finder} installed on sys.meta_path')

def remove_meta(address):
    if address in _installed_meta_cache:
        finder = _installed_meta_cache.pop(address)
        sys.meta_path.remove(finder)
        log.debug(f'{finder} removed from sys.meta_path')

class UrlPathFinder(importlib.abc.PathEntryFinder):
    def __init__(self, baseurl):
        self._link = None
        self._loader = UrlModuleLoader(baseurl)
        self._baseurl = baseurl

    def find_loader(self, fullname):
        log.debug(f'find_loader: {fullname}')
        parts = fullname.split('.')
        basename = parts[-1]
        if self._links is None:
            self._links = []
            self._links = _get_links(self._baseurl)

        if basename in self._links:
            log.debug(f'find_loader: trying package {fullname}')
            fullurl = self._baseurl + '/' + basename
            loader = UrlPackageLoader(fullurl)
            try:
                loader.load_module(fullname)
                log.debug(f'find_loader: package {fullname} loaded')
            except Exception as e:
                log.debug(f'find_loader: {fullname} is a namespace package')
            loader = None
            return (loader, [fullurl])

        filename = basename + '.py'
        if filename in self._links:
            log.debug(f'find_loader: module {fullname} found')
            return (self._loader, [])
        else:
            log.debug(f'find_loader: module {filename} not found')
            return (None, [])

    def invalidate_caches(self):
        log.debug('invalidating link cache')
        self._links = None

_url_path_cache = {}
def handle_url(path):
    if path.startswith(('http://', 'https://')):
        log.debug(f'Handle path? {path} [Yes]')
        if path in _url_path_cache:
            finder = _url_path_cache[path]
        else:
            finder = UrlPathFinder(path)
            _url_path_cache[path] = finder
        return finder
    else:
        log.debug(f'Handle path? {path} [No]')

def install_path_hook():
    sys.path_hooks.append(handle_url)
    sys.path_importer_cache.clear()
    log.debug('Installing handle_url')

def remove_path_hook():
    sys.path_hooks.remove(handle_url)
    sys.path_importer_cache.clear()
    log.debug('Removing handle_url')