<h1> Context </h1>
<p> Work done during the course of in my Master's in Languages and Knowledge Representation at University of Minho.
</p>

<h1> Problem </h1>
<p> Create a way to visualize ontologies in HTML using python as the base to the solution</p>

<h2> Solution</h2>
<p>A python script using several libraries including graphviz dot that outputs a simple HTML page that allows to explore the ontologie
content without the need to load it into a database engine or a ontologie editor like Protege  </p>
<p> The input format must be in rdf and this solution was made directed to small/medium ontologies, otherwise the graphs will be confusing</p>

<h2> Instalation</h2>

<p>pip install rdf2html</p>
<h2> Current use </h2>
<p>import rdf2html</p>
<p>from rdf2html import translator</p>
<p> translator.exec(["path_to_rdf/rdf_file.rdf"])</p>
<h1> Contributor </h1>
<p> <a href="https://github.com/sir-onze">Tiago Baptista</a></p>
