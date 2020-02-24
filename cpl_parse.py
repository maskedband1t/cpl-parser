#!/usr/bin/env python3
import click, csv, re
from anytree import Node, RenderTree

@click.command()
@click.argument(
    'domain_file',
    type=click.File('r')
)
@click.argument(
    'cpl_file',
    type=click.File('r')
)

def main(domain_file, cpl_file):
    write_cpl(cpl_file)
    domain_list = get_domains(domain_file)

    with open("cpl_domain_trees.txt", 'w') as trees:
        trees.close()

    for domain in domain_list:
        print(domain)
        root = Node(domain)
        buildTree(root, domain)

        with open("cpl_domain_trees.txt", 'a+') as trees:
            for pre, _, node in RenderTree(root):
                trees.write("%s%s" % (pre, node.name))
                trees.write("\n\n")
            trees.write("\n\n")
            print(' tree written in ./cpl_domain_trees.txt\n')


def buildTree(node, rel_root):
    '''
	builds tree down from given relative root node and writes it to output file

	Input: rel_root (string)
	Output: N/A
	'''

    results = getSupers(rel_root)
    _results = getSupers('"' + rel_root + '"')
    for _result in _results:
        results.append(_result)
    
    
    while results:
        for result in results:
            tempNode = Node(result, parent=node)
            buildTree(tempNode, result)
        results = []


def getSupers(nodeName):
    '''
	returns the supergroup(s) (tree-child) of the given node

	Input: nodeName(string) - name of the node to find the super of
	Output: supergroup (string) - super condition/category
	'''
    supergroups = []
    _define = "define c(.*)(.*)"
    define_regex = re.compile(_define)

    _end = "(end)([\s])"
    end_regex = re.compile(_end)

    super_regex = re.compile('([= \s!(])(' + nodeName + ')([\s ,)])')

    definition=False

    with open('cpl.txt', 'r') as cpl_file:
        define_line = 0
        for i, line in enumerate(cpl_file):

            define_result = define_regex.search(line)
            if define_result != None:
                _super = removeGroupPrefix(define_result.group(1))
                definition=True
                define_line = i
            end_result = end_regex.search(line)
            if end_result != None:
                definition=False


            match = super_regex.search(line)
            if match != None and definition == True:
                if not(i == define_line):
                    supergroups.append(_super)
        return supergroups


def write_cpl(cpl_file):
    '''
	writes cpl file input to static file bc of click b.s

	Input: CPL File (txt)
	Output: N/A
	'''
    if cpl_file:
        text = cpl_file.read()
        cpl_file = open('cpl.txt' , 'w')
        cpl_file.write(text)

def get_domains(domain_file):
    '''
	receives domain file input and returns a list of all the domains

	Input: comma-separated domains file (txt)
	Output: domains (list)
	'''
    if domain_file:
        text = domain_file.read()
        return text.split(',')

def removeGroupPrefix(grouping):
    '''
    strips part of a regex returned group for what the group's name actually is bc I hate regex

	Input: grouping(string)
	Output: stripped grouping (string)
	'''
    if grouping.startswith('ondition'):
        return grouping[9:]
    elif grouping.startswith('ategory'):
        return grouping[8:]
    else:
        return grouping

if __name__ == '__main__':
    main()
