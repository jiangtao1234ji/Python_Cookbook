import collections
import re
from macpath import dirname

__author__ = 'kerman jt'

# line = 'asdf sadas; asdfasa  asfas, fasdasf,          sdaf'
# print(line.split())
# import re
#
# print(re.split(r'[;,\s]\s*', line))
# fields = re.split(r'(;|,|\s)\s*', line)
# print(fields)
# value = fields[::2]
# print(fields[1::2])
# print(re.split(r'(?:,|;|\s)\s*', line))


# filename = 'sapm.txt'
# print(filename.endswith('.txt'))
# url = 'http://www.baidu.com'
# print(url.startswith('http:'))
# import os
#
# filename = os.listdir('.')
# print(filename)
# print([name for name in filename if name.endswith(('.c', '.cpp'))])
# print(any(name.endswith('.py') for name in filename))
#
# from urllib.request import urlopen
#
#
# def read_data(name):
#     if name.startswith(('https:', 'http:', 'ftp:')):
#         return urlopen(name).read()
#     else:
#         with open(name) as f:
#             return f.read()
#
#
# url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:'
# re.match('http:|https:|ftp:', url)
# if any(name.endswith('.c', '.cpp', '.py') for name in os.listdir(dirname)):
#     print('yes')


# from fnmatch import fnmatch
# names = ['Dat1.csv', 'Dat2.csv', '1.py', '2.c']
# print([name for name in names if fnmatch(name, 'Dat*.csv')])


# datepat = re.compile(r'\d+/\d+/\d+')
#
# text = '11/2/2018    22/1/2019'
# print(datepat.match(text), datepat.findall(text))

# text = 'Today is 18/5/2019. PyCon statrs 13/3/2013'
# import re
#
# print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\2-\1', text))
#
# from calendar import month_abbr
#
#
# def change_date(m):
#     mon_name = month_abbr[int(m.group(2))]
#     return '{} {} {}'.format(m.group(1), mon_name, m.group(3))
#
#
# print(re.sub(r'(\d+)/(\d+)/(\d+)', change_date, text))
# newtext, n = re.subn(r'(\d+)/(\d+)/(\d+)', r'\3-\2-\1', text)
# print(newtext, n)


# text = 'UPPER PYTHON, lower python, Mixed Python'
# print(re.findall('python', text, flags=re.IGNORECASE))
# print(re.sub('python', 'snake', text, flags=re.IGNORECASE))
#
#
# def matchcase(word):
#     def replace(m):
#         text = m.group()
#         if text.isupper():
#             return word.upper()
#         elif text.islower():
#             return word.lower()
#         elif text[0].isupper():
#             return word.capitalize()
#         else:
#             return word
#     return replace
#
#
# print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))


# str_pat = re.compile(r'\"(.*)\"')
# text1 = 'Computer says "no."'
# print(str_pat.findall(text1))
# text2 = 'Computer says "no." Phone says "yes."'
# print(str_pat.findall(text2))
# str_pat = re.compile(r'\"(.*?)\"')
# print(str_pat.findall(text2))


# text = '''/* this is a
#             multiline comment*/
# '''
# comment = re.compile(r'/\*((?:.|\n)*?)\*/')
# print(comment.findall(text))
# comment = re.compile(r'/\*((.|\n)*?)\*/')
# print(comment.findall(text))


# s1 = 'Spicy Jalape\u00f1o'
# s2 = 'Spicy Jalapen\u0303o'
# import unicodedata
# t1 = unicodedata.normalize('NFD', s1)
# t2 = unicodedata.normalize('NFC', s2)
# print(''.join(c for c in t1 if not unicodedata.combining(c)))


# s = 'python\fis\tawesome\r\n'
# print(s)
# remap = {
#     ord('\t') : ' ',
#     ord('\f') : ' ',
#     ord('\r') : None
# }
# a = s.translate(remap)
# print(a)


# text = ' Hello World    '
# print(format(text, '>20'))
# print(format(text, '<20'))
# print(format(text, '^20'))
# print(format(text, '=<20'))
# data = ['ACME', 50, 91.1]
# print(' '.join(str(d) for d in data))
# a = 'Today'
# b = 'is'
# c = 'a'
# '''ugly'''
# print(a + ':' + b + ':' + c)
# '''still ugly'''
# print(':'.join([a, b, c]))
# '''Better'''
# print(a, b, c, sep=':')


# s = 'Elements are written as "<tag>text</tag>".'
# import html
# print(s)
# print(html.escape(s))


# text = 'foo = 23  + 42 * 10'
# tokens = {('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'),
#           ('NUM', '42'), ('TIMES', '*'), ('NUM'), '10'}
# NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
# NUM = r'(?P<NUM>\d+)'
# PLUS = r'(?P<PLUS>\+)'
# TIMES = r'(?P<TIMES>\*)'
# EQ = r'(?P<EQ>=)'
# WS = r'(?P<WS>\s+)'
# master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
# from collections import namedtuple
# Token = namedtuple('Token', ['type', 'value'])
# def generate_tokens(pat, text):
#     scanner = pat.scanner(text)
#     for m in iter(scanner.match, None):
#         yield Token(m.lastgroup, m.group())
# for tok in generate_tokens(master_pat, 'foo = 42'):
#     print(tok)
# tokens = (tok for tok in generate_tokens(master_pat, 'foo = *') if tok.type != 'WS')
# for tok in tokens:
#     print(tok)


NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>-)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES, DIVIDE,
                                  LPAREN, RPAREN, WS]))
Token = collections.namedtuple('Token', ['type', 'value'])


def generate_tokens(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != 'WS':
            yield tok


class ExpressionEvaluator:
    def parse(self, text):
        self.tokens = generate_tokens(text)
        self.tok = None
        self.nexttok = None
        self._advance()
        return self.expr()

    def _advance(self):
        'Advance one token ahead'
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

    def _accept(self, toktype):
        'Test and consume the next token if it matches toktype'
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False

    def _expect(self, toktype):
        'Consume next token if it matches toktype or raise SyntaxError'
        if not self._accept(toktype):
            raise SyntaxError('Expected' + toktype)

    def expr(self):
        "expression ::= term { ('+'|'-') term }*"
        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval += right
            elif op == 'MINUS':
                exprval -= right
        return exprval

    def term(self):
        "term ::= factor { ('*' | '/') factor }*"
        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval *= right
            elif op == 'DIVIDE':
                termval /= right
        return termval

    def factor(self):
        "factor ::= NUM | (expr)"
        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUMBER or LPAREN')


e = ExpressionEvaluator()
print(e.parse('20-10/8'))

