#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Bazzinator v0.1 """

import sys
import os
import json
import cgi, cgitb
import random

random.seed()

mumbles = ['mbrrmb', 'fbrbrg', 'rigga', 'digga', 'mmmmrbu', 'mmbbzz', 'mmbrmmm']
randomness = ['<em>ACTUALLY</em>', 'hurhurhur', 'chacaron', 'Uhhh, NO!', 'Ola', '<strong>I think you\'ll find</strong>', '<strong>For <em>Gods</em> sake</strong>']

form = cgi.FieldStorage()
print 'Content-Type: text/html\n'

# Set our output streams
sys.stderr = sys.stdout

print '<!doctype html>'
print '<html>'
print '  <head>'
print '    <meta charset="UTF-8">'
print '    <title>Curiola Presents: The Bazzinator</title>'
print '    <meta name="viewport" content="width=device-width, initial-scale=1.0">'
print '    <meta name="description" content="Turns your rubbish into Works of Baz">'
print '    <meta name="author" content="Curiola">'
print '     <!--[if lt IE 9]>'
print '    <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>'
print '    <![endif]-->'
print '    <link href="bootstrap.css" rel="stylesheet">'
print '    <style>'
print '    textarea { width: 100%; border: 1px solid #333; padding: 4px; }'
print '    </style>'
print '  </head>'
print '<body>'
print '<div class="container">'
print '  <div class="jumbotron">'
print '    <h1>The Bazzinator</h1>'
print '    <p class="lead">Turns your rubbish human words into Works of Baz</p>'
print '  </div>'


def bazit(tobebazzed):
	the_mumble = ""
	for i in tobebazzed.split():
		the_mumble += "%s%s" % (random.choice(mumbles),i.lower()) + " "
		if random.random() < 0.1:
			the_mumble += "%s " % (random.choice(randomness))
	return the_mumble;

def theEscaper(dirtyString):
    escapees = {'\"' : '&quot;',
                '\'' : '&#39;',
                '<'  : '&lt;',
                '>'  : '&gt;'}
    dirtyString = dirtyString.replace('&', '&amp;')
    for badValue, escapedValue in escapees.iteritems():
        dirtyString = dirtyString.replace(badValue, escapedValue)
    return dirtyString


# What's that? New data? YUMMY!
if form.getvalue('paste'):
	print '<div class="row marketing">'
	print '<div class="span10 offset2">'
	thePaste = form.getvalue('paste')
	print '<h2>You what Baz?</h2>'
	print '</div>'
	print '</div>'

	print '<div class="row">'
	print '<div class="col-lg-2">'
	print '<img src="Bazmbr.gif" />'
	print '</div>'
	print """<style>
  .bubble {
    position: relative;
    width: 80%;
    padding: 10px;
    background: #efefef;
    -webkit-border-radius: 10px;
    -moz-border-radius: 10px;
    border-radius: 10px;
    -webkit-box-shadow: 0px 2px 21px 0px #616161;
    -moz-box-shadow: 0px 2px 21px 0px #616161;
    box-shadow: 0px 2px 21px 0px #616161;
}

  .bubble:after {
    content: "";
    position: absolute;
    top: 10px;
    left: -20px;
    border-style: solid;
    border-width: 15px 20px 15px 0;
    border-color: transparent #efefef;
    display: block;
    width: 0;
    z-index: 1;
}

</style>
"""
	print '<div class="col-lg-10">'
	print '<div class="bubble">'
	print "<p><em>" + bazit(theEscaper(thePaste)) + "</em></p>"
	print '</div>'
	print '</div>'

print '<div class="col-lg-12">'

# Ask for more!
print '<h3>What do you want to talk about with Baz?</h3>'
print '<form class="well" action="bazzinator.py" method="post">'
print '<textarea name="paste" rows="20" placeholder="Paste here...">'
print '</textarea>'
print '<hr />'
print '<input class="btn btn-lg btn-success" type="submit" value="le bazzinate" />' 
print '</form>'

print '</div>'
print '<!-- Placed at the end of the document so the pages load faster -->'
print '<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>'
print '<script src="bootstrap.min.js"></script>'
print '</body>'
print '</html>'
