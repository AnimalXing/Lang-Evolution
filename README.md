# Lang-Evolution

This program is designed to examine the historical phonology changes between two languages by creating a Sankey diagram. The program takes in several parameters:

    parent_doc: the name of the excel file that contains the parent language
    child_doc: the name of the excel file that contains the child language
    parent_char: the column name in parent_doc that contains the characters of the parent language
    child_char: the column name in child_doc that contains the characters of the child language
    parent_conso: the column name in parent_doc that contains the consonants of the parent language
    child_conso: the column name in child_doc that contains the consonants of the child language
    title: the title of the Sankey diagram
    anomaly: an optional parameter that sets a threshold for the minimum number of occurrences for a consonant change to be plotted in the diagram. Default value is 0.

The program starts by reading the excel files specified by parent_doc and child_doc, and creating new dataframes df1_new and df2_new that contain the relevant columns of characters and consonants. These dataframes are then merged on the character column to create a new dataframe merged_df. The program then groups the data by the consonant changes and counts the number of occurrences. This data is used to create a Sankey diagram using the Plotly library. The diagram shows the flow of consonant changes between the parent and child languages. The color of the links in the diagram are determined by their source and target nodes.

The program also includes a feature that allows you to filter out changes that have a low number of occurrences by using the anomaly parameter.

To use this program, you will need to have the following libraries installed:

    pandas
    plotly

You will also need to have the data in excel file format, with columns containing characters and consonants in the format specified in the parameters. Once you have the data and the dependencies, you can call the function lang_evo_sankey and pass in the appropriate parameters to generate the Sankey diagram.

One example of the Sankey diagram can be found here: 

[Middle Chinese](https://en.wikipedia.org/wiki/Middle_Chinese) vs. Lishuinese (a dialect of [Wu](https://en.wikipedia.org/wiki/Wu_Chinese)) <img width="1826" alt="image" src="https://user-images.githubusercontent.com/66161458/215300278-4ca4dee9-7422-4be2-97b7-96b35e856ff4.png">

A sample input of parent_doc & child_doc is as follows:

Parent_doc: (Old English) 

|   | word      | modern_word | consonant |
|---|-----------|-------------|-----------|
| 0 | bēon      | be          | b         |
| 1 | cūð       | couth       | c         |
| 2 | dæġ       | day         | d         |
| 3 | fisc      | fish        | f         |
| 4 | gōd       | good        | g         |
| 5 | hring     | ring        | h         |
| 6 | lēoht     | light       | l         |
| 7 | mūs       | mouse       | m         |
| 8 | nēowol    | newfangled  | n         |
| 9 | pyle      | pile        | p         |
| 10| rēad      | red         | r         |
| 11| sāwan     | sow         | s         |
| 12| þorn     | thorn       | þ         |
| 13| wæstm     | waste       | w         |

Child_doc: (Modern English)

|   | word      | consonant |
|---|-----------|-----------|
| 0 | be        | b         |
| 1 | couth     | c         |
| 2 | day       | d         |
| 3 | fish      | f         |
| 4 | good      | g         |
| 5 | ring      | r         |
| 6 | light     | l         |
| 7 | mouse     | m         |
| 8 | newfangled| n         |
| 9 | pile      | p         |
| 10| red       | r         |
| 11| sow       | s         |
| 12| thorn     | th        |
| 13| waste     | w         |
