#HELLO AND WELCOME TO THE READ.ME for TextCutUps

This package lets you create 'cut ups' with text in the style of William Burroughs. I had always wanted to make a package that does this, so thought I'd have a try. this can let you arrange text in new ways where you may get surprising new connections between lines etc.

INSTALLING

do a pip install textcutups

then:

from Textcutpackage import textcuts

THE PACKAGE CONTENTS

 The package lets you do this through a few ways. Depending on the way you choose you may need to import textwrap from python or install nltk and import it's sent_tokenize.

Okay so here are  the ways you can cut up text:

- Cutting a page into 4 sections by sentence (you will first need to install nltk package and import sent_tokenize). This method will take each sentence and use this to create the sections.
- Cutting a page into 4 sections by line (you will need to import textwrap from python to get this working). This method takes each line and cuts it, in order to make the sections
- Creating a fold from two texts (you will need to also import textwrap to get this working). This method puts a cut down the middle of a page. You can then combine the two texts.

You can also play with the parameters for each function. However for each one you will need to have stored your text as 'texts'. Or enter the text as a 'string'


**- linecutup() is the function that cuts up by lines**

Here you will have the parameters
- **texts** : this is where you store your text in a previous variable, this will go first
- **line** : this lets you detrmine the length of the line read in. The default is 80 characters long
- **cut** : this let's you say where you want the cut to be made. 
0.2 will be 20% of the way through the line
0.5 will be 50% of the way throguh the line
0.8 will be 80% of the way through the line
and so on. The default is 0.5 which makes a cut 50% through the line
- **order** : this will let you choose which order to rearrange the text in. Currently these are preset orders, so you pick either 1,2, 3 or 4. By Default it is set to 1. There is more information on orders toward the bottom of the page.

EXAMPLE: linecutup(texts,line = 80,cut = 0.5,order = 1)

**foldtext() has a similar approach**

However for this function you will have two texts. e.g.

foldtext (text1, text2, line, cut, order = 1)

The parameters are again the same

Here you will have the parameters
- **text1** : this is where you store your first text
- **text2** : this is where you store your first text
- **line** : this lets you detrmine the length of the line read in. Default is 80 characters
- **cut** : this let's you say where you want the cut to be made.
0.2 will be 20% of the way through the line
0.5 will be 50% of the way throguh the line
0.8 will be 80% of the way through the line
and so on. The default is 0.5 which makes a cut 50% through the line
- **order** : this will let you choose which order to rearrange the text in. Currently these are preset orders, so you pick either 1,2, 3 or 4. By default it is set to 1.

- cutsent() is the version that uses sentences (you will need to install nltk package to do this and use its sent_tokenize). This version also has less parameters than the other options currently.

##A little note on orders.##
 - Here the page is essentially split into 4 sections and named A1,A2,B1 B2. If we were looking at the page this would be splitting it into

 - A1 A2
 - B1 B2

 Once the page has been cut into these sections you can then rearrange them. E.g

 if we start with the below sections

 - A1 A2
 - B1 B2

it could be rearranged to:

- B2 A2
- B1 A1


