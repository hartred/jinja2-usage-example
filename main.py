#!/usr/bin/env python3

from jinja2 import Template


def main():
    with open('index.jinja') as tmpl:
        template = Template(tmpl.read())
    
    cats = []

    for i in range(1, 4):
        with open(f'descriptions/cat{i}.txt') as f:
            cats.append(dict(
                path=f'images/cat{i}.jpg',
                title=f'cat{i}',
                description=f.read()
            ))
    
    template.stream(cats=cats).dump('index.html')

if __name__ == '__main__':
    main()
