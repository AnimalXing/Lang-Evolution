#This is a python program that examine the historical phonology changes between two languages

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import ssl
ssl._create_default_https_context = ssl._create_unverified_context



def lang_evo_sankey(parent_doc,child_doc,parent_char,child_char,parent_conso,child_conso,title,anomaly=0):
    df1 = pd.read_excel(parent_doc)# name of a excel (xls, xlsx etc.) file that contains the parent language
    df2 = pd.read_excel(child_doc) # name of a excel (xls, xlsx etc.) file that contains the parent language
    df1_new = df1[[parent_char,parent_conso]]
    df2_new = df2[[child_char,child_conso]]
    df2_new.columns = [parent_char,child_conso]
    merged_df = df2_new.merge(df1_new, how='inner', on=[parent_char])
    df_count = merged_df.groupby([parent_conso, child_conso])[parent_char].count().reset_index()
    df_count.columns = ['source', 'target', 'value']
    print(df_count)
    links = df_count
    print(links, "links\n")
    unique_source_target = list(pd.unique(links[['source', 'target']].values.ravel('K')))
    unique_source_count = len(list(pd.unique(links[['source']].values.ravel('K'))))
    unique_target_count = len(list(pd.unique(links[['target']].values.ravel('K'))))
    print(unique_source_target,"\n")

    mapping_dict = {k: v for v, k in enumerate(unique_source_target)}

    print(mapping_dict, "map\n")

    links['source'] = links['source'].map(mapping_dict)
    links['target'] = links['target'].map(mapping_dict)
    print(links)

    drop_l = []

    for index, row in links.iterrows():
        if row["value"] <= anomaly:
            drop_l.append(index)
    print(drop_l)
    links = links.drop(drop_l).reset_index(drop=True)

    links_dict = links.to_dict(orient='list')

    print(links_dict)

    named_colorscales = ['rgba(251,180,174,0.8)', 'rgba(179,205,227,0.8)', 'rgba(204,235,197,0.8)','rgba(222,203,228,0.8)', 'rgba(254,217,166,0.8)', 'rgba(255,255,204,0.8)', 'rgba(229,216,189,0.8)', 'rgba(253,218,236,0.8)', 'rgba(242,242,242,0.8)']
    all_colour = []
    source_colour = []

    #define colours of nodes (same for one consonant) and flows 

    for i in range(len(links['source'])):
        mod = links['source'][i] % (len(named_colorscales))
        colour = named_colorscales[mod]
        all_colour.append(colour)
    for i in range(unique_source_count):
        mod = i % (len(named_colorscales))
        colour = named_colorscales[mod]
        source_colour.append(colour)
    for i in range(unique_target_count):
        source_colour.append("white")




    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color='rgba(0,0,0,0)', width=0.1),
            label=unique_source_target,
            color= source_colour
        ),
        link=dict(
            source=links_dict["source"],
            target=links_dict["target"],
            value=links_dict["value"],
            color = all_colour

        ))])
    fig.update_layout(title_text=title, font_size=10)
    fig.show()
