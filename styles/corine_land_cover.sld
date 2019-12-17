<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" version="1.0.0" xmlns:sld="http://www.opengis.net/sld">
  <UserLayer>
    <sld:LayerFeatureConstraints>
      <sld:FeatureTypeConstraint/>
    </sld:LayerFeatureConstraints>
    <sld:UserStyle>
      <sld:Name>landcover2018</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:ChannelSelection>
              <sld:GrayChannel>
                <sld:SourceChannelName>1</sld:SourceChannelName>
              </sld:GrayChannel>
            </sld:ChannelSelection>
            <sld:ColorMap type="ramp">
              <sld:ColorMapEntry quantity="111" color="#e6004d" label="Continuous urban fabric"/>
              <sld:ColorMapEntry quantity="112" color="#ff0000" label="Discontinuous urban fabric"/>
              <sld:ColorMapEntry quantity="121" color="#cc4df2" label="Industrial or commercial units"/>
              <sld:ColorMapEntry quantity="122" color="#cc0000" label="Road and rail networks and associated land"/>
              <sld:ColorMapEntry quantity="123" color="#e6cccc" label="Port areas"/>
              <sld:ColorMapEntry quantity="124" color="#e6cce6" label="Airports"/>
              <sld:ColorMapEntry quantity="131" color="#a600cc" label="Mineral extraction sites"/>
              <sld:ColorMapEntry quantity="132" color="#a64d00" label="Dump sites"/>
              <sld:ColorMapEntry quantity="133" color="#ff4dff" label="Construction sites"/>
              <sld:ColorMapEntry quantity="141" color="#ffa6ff" label="Green urban areas"/>
              <sld:ColorMapEntry quantity="142" color="#ffe6ff" label="Sport and leisure facilities"/>
              <sld:ColorMapEntry quantity="211" color="#ffffa8" label="Non-irrigated arable land"/>
              <sld:ColorMapEntry quantity="212" color="#ffff00" label="Permanently irrigated land"/>
              <sld:ColorMapEntry quantity="213" color="#e6e600" label="Rice fields"/>
              <sld:ColorMapEntry quantity="221" color="#e68000" label="Vineyards"/>
              <sld:ColorMapEntry quantity="222" color="#f2a64d" label="Fruit trees and berry plantations"/>
              <sld:ColorMapEntry quantity="223" color="#e6a600" label="Olive groves"/>
              <sld:ColorMapEntry quantity="231" color="#e6e64d" label="Pastures"/>
              <sld:ColorMapEntry quantity="241" color="#ffe6a6" label="Annual crops associated with permanent crops"/>
              <sld:ColorMapEntry quantity="242" color="#ffe64d" label="Complex cultivation patterns"/>
              <sld:ColorMapEntry quantity="243" color="#e6cc4d" label="Land principally occupied by agriculture with significant areas of natural vegetation"/>
              <sld:ColorMapEntry quantity="244" color="#f2cca6" label="Agro-forestry areas"/>
              <sld:ColorMapEntry quantity="311" color="#80ff00" label="Broad-leaved forest"/>
              <sld:ColorMapEntry quantity="312" color="#00a600" label="Coniferous forest"/>
              <sld:ColorMapEntry quantity="313" color="#4dff00" label="Mixed forest"/>
              <sld:ColorMapEntry quantity="321" color="#ccf24d" label="Natural grasslands"/>
              <sld:ColorMapEntry quantity="322" color="#a6ff80" label="Moors and heathland"/>
              <sld:ColorMapEntry quantity="323" color="#a6e64d" label="Sclerophyllous vegetation"/>
              <sld:ColorMapEntry quantity="324" color="#a6f200" label="Transitional woodland-shrub"/>
              <sld:ColorMapEntry quantity="331" color="#e6e6e6" label="Beaches dunes sands"/>
              <sld:ColorMapEntry quantity="332" color="#cccccc" label="Bare rocks"/>
              <sld:ColorMapEntry quantity="333" color="#ccffcc" label="Sparsely vegetated areas"/>
              <sld:ColorMapEntry quantity="334" color="#000000" label="Burnt areas"/>
              <sld:ColorMapEntry quantity="335" color="#a6e6cc" label="Glaciers and perpetual snow"/>
              <sld:ColorMapEntry quantity="411" color="#a6a6ff" label="Inland marshes"/>
              <sld:ColorMapEntry quantity="412" color="#4d4dff" label="Peat bogs"/>
              <sld:ColorMapEntry quantity="421" color="#ccccff" label="Salt marshes"/>
              <sld:ColorMapEntry quantity="422" color="#e6e6ff" label="Salines"/>
              <sld:ColorMapEntry quantity="423" color="#a6a6e6" label="Intertidal flats"/>
              <sld:ColorMapEntry quantity="511" color="#00ccf2" label="Water courses"/>
              <sld:ColorMapEntry quantity="512" color="#80f2e6" label="Water bodies"/>
              <sld:ColorMapEntry quantity="521" color="#00ffa6" label="Coastal lagoons"/>
              <sld:ColorMapEntry quantity="522" color="#a6ffe6" label="Estuaries"/>
              <sld:ColorMapEntry quantity="523" color="#e6f2ff" label="Sea and ocean"/>
              <sld:ColorMapEntry quantity="999" color="#ffffff" label="NODATA"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </UserLayer>
</StyledLayerDescriptor>
