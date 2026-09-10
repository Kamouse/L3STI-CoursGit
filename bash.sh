bash 

echo 'graph G {
  graph [bgcolor="transparent", rankdir=LR, nodesep=0.5, ranksep=0.8]
  node [shape=circle, style="filled", fontname="Helvetica", fontsize=14, penwidth=3]
  edge [color="#687386", penwidth=3]

  A [fillcolor="#fff5f5", color="#e3262e", label="A"]
  B [fillcolor="#fff5f5", color="#e3262e", label="B"]
  C [fillcolor="#eef4ff", color="#2864e8", label="C"]
  D [fillcolor="#fff5f5", color="#e3262e", label="D"]

  A -- B
  B -- C
  B -- D

  topic [shape=box, style="rounded,filled", fillcolor="#2864e8", color="#2864e8", fontcolor="white", label="topic"]
  main [shape=box, style="rounded,filled", fillcolor="#e3262e", color="#e3262e", fontcolor="white", label="main"]

  topic -- C [style=invis]
  main -- D [style=invis]
}' | dot -Tsvg | chafa -f symbols --colors 256 -s 100x35
