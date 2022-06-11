<h1>Markdown to HTML</h1>

<p>
  This is the implementation I wrote my self that converts markdown text to html.
</p>
<h3>These are the capabilities of my converter:</h3>

<h4>Headings</h4>
<pre><code>guillaume@vagrant:~/$ cat README.md
# My title
## My title2
# My title3
#### My title4
### My title5
guillaume@vagrant:~/$ ./markdown2html.py README.md README.html 
guillaume@vagrant:~/$ cat README.html 
&lt;h1&gt;My title&lt;/h1&gt;
&lt;h2&gt;My title2&lt;/h2&gt;
&lt;h1&gt;My title3&lt;/h1&gt;
&lt;h4&gt;My title4&lt;/h4&gt;
&lt;h3&gt;My title5&lt;/h3&gt;
guillaume@vagrant:~/$ 
</code></pre>

<h4>Unordered listing</h4>
<pre><code>guillaume@vagrant:~/$ cat README.md
# My title
- Hello
- Bye
guillaume@vagrant:~/$ ./markdown2html.py README.md README.html 
guillaume@vagrant:~/$ cat README.html 
&lt;h1&gt;My title&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;Hello&lt;/li&gt;
&lt;li&gt;Bye&lt;/li&gt;
&lt;/ul&gt;
guillaume@vagrant:~/$ 
</code></pre>


<h4>Ordered listing </h4>
<pre><code>guillaume@vagrant:~/$ cat README.md
# My title
* Hello
* Bye

guillaume@vagrant:~/$ ./markdown2html.py README.md README.html 
guillaume@vagrant:~/$ cat README.html 
&lt;h1&gt;My title&lt;/h1&gt;
&lt;ol&gt;
&lt;li&gt;Hello&lt;/li&gt;
&lt;li&gt;Bye&lt;/li&gt;
&lt;/ol&gt;
guillaume@vagrant:~/$ 
</code></pre>

<h4>Simple text</h4>
<pre><code>guillaume@vagrant:~/$ cat README.md
# My title
- Hello
- Bye

Hello

I'm a text
with 2 lines
guillaume@vagrant:~/$ ./markdown2html.py README.md README.html 
guillaume@vagrant:~/$ cat README.html 
&lt;h1&gt;My title&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;Hello&lt;/li&gt;
&lt;li&gt;Bye&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;
Hello
&lt;/p&gt;
&lt;p&gt;
I'm a text
&lt;br/&gt;
with 2 lines
&lt;/p&gt;
guillaume@vagrant:~/$ 
</code></pre>

<h1>Developer</h1>
<p>Mbuke Prince</p>
