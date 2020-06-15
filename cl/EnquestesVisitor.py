# Generated from Enquestes.g4 by ANTLR 4.7.2
import pickle
import networkx as nx
import matplotlib.pyplot as plt

from antlr4 import *
if __name__ is not None and "." in __name__:
    from .EnquestesParser import EnquestesParser
else:
    from EnquestesParser import EnquestesParser


# This class defines a complete generic visitor for a parse tree produced by EnquestesParser.
class EnquestesVisitor(ParseTreeVisitor):
    global edgeItem
    global dictItem
    global nodePreg
    global nodeRes
    global edgePreg
    global edgeAltern
    global prohibits
    global G

    # Visit a parse tree produced by EnquestesParser#r.
    def visitR(self, ctx: EnquestesParser.RContext):
        self.G = nx.DiGraph()
        self.edgeItem = []
        self.edgePreg = []
        self.nodePreg = []
        self.nodeRes = []
        self.prohibits = []
        self.dictItem = {}
        self.edgeAltern = []
        return self.visitChildren(ctx)

    # Visit a parse tree produced by EnquestesParser#tanda.
    def visitTanda(self, ctx: EnquestesParser.TandaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by EnquestesParser#pregunta.
    def visitPregunta(self, ctx: EnquestesParser.PreguntaContext):
        IDPregunta = next(ctx.getChildren()).getText()
        n = ctx.getChildren()
        l = [next(n) for i in range((ctx.getChildCount()))]
        preg = ">"
        for i in range((ctx.getChildCount())):
            if (i == ctx.getChildCount()-1):
                preg = preg+(l[i].getText())
            elif (i != 0 and i != 1 and i != 2):
                preg = preg+(" ")+(l[i].getText())
        self.nodePreg.append(IDPregunta)
        self.G.add_node(IDPregunta, tipus='pregunta', p=preg)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by EnquestesParser#resposta.
    def visitResposta(self, ctx: EnquestesParser.RespostaContext):
        IDResposta = next(ctx.getChildren()).getText()
        n = ctx.getChildren()
        l = [next(n) for i in range((ctx.getChildCount()))]
        resp = ""
        for i in range((ctx.getChildCount())):
            primer = True
            if (i == ctx.getChildCount()-1):
                if (primer):
                    resp = resp+(self.visit(l[i]))
                    primer = False
                else:
                    resp = resp + (" ") + (self.visit(l[i]))
        self.nodeRes.append(IDResposta)
        self.G.add_node(IDResposta, tipus='resposta', r=resp)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by EnquestesParser#opcions.
    def visitOpcions(self, ctx: EnquestesParser.OpcionsContext):
        n = ctx.getChildren()
        l = [next(n) for i in range((ctx.getChildCount()))]
        opc = ""
        for i in range((ctx.getChildCount())):
            if (i == 0):
                opc = opc+(l[i].getText())
            else:
                opc = opc+(" ")+(l[i].getText())
        return opc

    # Visit a parse tree produced by EnquestesParser#item.
    def visitItem(self, ctx: EnquestesParser.ItemContext):
        Item = next(ctx.getChildren()).getText()
        n = ctx.getChildren()
        l = [next(n) for i in range(6)]
        ItemPreg = l[3].getText()
        ItemRes = l[5].getText()
        TupleItem = tuple([ItemPreg, ItemRes])
        self.dictItem[Item] = TupleItem
        self.edgeItem.append(TupleItem)
        self.G.add_edge(ItemPreg, ItemRes, tipus='item', range=Item)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by EnquestesParser#alternativa.
    def visitAlternativa(self, ctx: EnquestesParser.AlternativaContext):
        n = ctx.getChildren()
        l = [next(n) for i in range(6)]
        Previa = l[3].getText()
        PregPrevia = self.dictItem[Previa][0]
        tupla = self.visit(l[5])
        for i in range(len(tupla)):
            self.prohibits.append(self.dictItem[tupla[i][1]][0])
            weight = tupla[i][0]
            TupleAltern = tuple([PregPrevia, self.dictItem[tupla[i][1]][0]])
            self.edgeAltern.append(TupleAltern)
            self.G.add_edge(PregPrevia, self.dictItem[tupla[i][1]][0], tipus='alternativa', number=weight)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by EnquestesParser#implicacio.
    def visitImplicacio(self, ctx: EnquestesParser.ImplicacioContext):
        llistatuplas = []
        n = ctx.getChildren()
        l = [next(n) for i in range(ctx.getChildCount())]
        for i in range(len(l)):
            if (i % 2 == 0):
                llistatuplas.append(self.visit(l[i]))
        return llistatuplas

    # Visit a parse tree produced by EnquestesParser#implicacions.
    def visitImplicacions(self, ctx: EnquestesParser.ImplicacionsContext):
        n = ctx.getChildren()
        l = [next(n) for i in range(ctx.getChildCount())]
        tupla = tuple([l[1].getText(), l[3].getText()])
        return tupla

    # Visit a parse tree produced by EnquestesParser#enquesta.
    def visitEnquesta(self, ctx: EnquestesParser.EnquestaContext):
        self.G.add_node(next(ctx.getChildren()).getText(), tipus='id', id=next(ctx.getChildren()).getText())
        self.nodePreg.insert(0, next(ctx.getChildren()).getText())
        n = ctx.getChildren()
        l = [next(n) for i in range(ctx.getChildCount())]
        self.G.add_node(l[ctx.getChildCount()-1].getText(), tipus='end', end=l[ctx.getChildCount()-1].getText())
        self.nodePreg.append(l[ctx.getChildCount()-1].getText())
        nodes = [x for x in self.nodePreg if x not in self.prohibits]
        for i in range(len(nodes)-1):
            self.edgePreg.append(tuple([nodes[i], nodes[i+1]]))
            self.G.add_edge(nodes[i], nodes[i+1], tipus='normal')
        labels = nx.get_edge_attributes(self.G, 'range')
        number = nx.get_edge_attributes(self.G, 'number')
        pos = nx.circular_layout(self.G)
        P = self.G.subgraph(self.nodePreg)
        R = self.G.subgraph(self.nodeRes)
        nx.draw_networkx_nodes(self.G, pos, nodelist=self.nodePreg)
        nx.draw_networkx_nodes(self.G, pos, nodelist=self.nodeRes)
        nx.draw_networkx_edges(self.G, pos, edgelist=self.edgePreg, edge_color='black')
        nx.draw_networkx_edges(self.G, pos, edgelist=self.edgeItem, edge_color='blue')
        nx.draw_networkx_edge_labels(self.G, pos, edgelist=self.edgeItem, edge_labels=labels, font_color='blue')
        nx.draw_networkx_edges(self.G, pos, edgelist=self.edgeAltern, edge_color='green')
        nx.draw_networkx_edge_labels(self.G, pos, edgelist=self.edgeAltern, edge_labels=number, font_color='green')
        nx.write_gpickle(self.G, "test.gpickle")
        nx.draw_networkx_labels(P, pos)
        nx.draw_networkx_labels(R, pos)
        plt.savefig('graf.png')
        plt.show()

        return self.visitChildren(ctx)

del EnquestesParser
