# Juridecomposer

The Juridecomposer package can be used to transform Dutch laws structured as .xml files into pandas dataframes. 
Input laws can be retrieved from [wetten.nl](https://wetten.overheid.nl/). 

# Example usage

    from juridecomposer.juridecomposer import xml_to_dataframe
    output_dataframe = xml_to_dataframe("path/to/law/xml")

The output dataframe will consist of the following columns:
- Brontekst: raw extracted text;
- Nummer: specifies the chapter (hoofdstuk) number;
- Lid: specificies the section (afdeling) number;
- Opsomming niveau 1: specifies the article (artikel) number;
- Opsomming niveau 2: specifies the component (onderdeel) number;
- Opsomming niveau 3: specifies the second component (onderdeel) number, if available; 
- Versie: specifies the version number;
- jc 1.3: permanent link to specific section.



