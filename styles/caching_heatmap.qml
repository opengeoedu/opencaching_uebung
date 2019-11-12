<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="1e+08" styleCategories="AllStyleCategories" maxScale="0" hasScaleBasedVisibilityFlag="0" version="3.8.2-Zanzibar">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <customproperties>
    <property value="false" key="WMSBackgroundLayer"/>
    <property value="false" key="WMSPublishDataSourceUrl"/>
    <property value="0" key="embeddedWidgets/count"/>
    <property value="Value" key="identify/format"/>
  </customproperties>
  <pipe>
    <rasterrenderer classificationMin="5" opacity="1" alphaBand="-1" type="singlebandpseudocolor" band="1" classificationMax="150">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <rastershader>
        <colorrampshader clip="0" classificationMode="2" colorRampType="INTERPOLATED">
          <colorramp type="gradient" name="[source]">
            <prop v="43,131,186,255" k="color1"/>
            <prop v="215,25,28,255" k="color2"/>
            <prop v="0" k="discrete"/>
            <prop v="gradient" k="rampType"/>
            <prop v="0.25;171,221,164,255:0.5;255,255,191,255:0.75;253,174,97,255" k="stops"/>
          </colorramp>
          <item value="5" alpha="255" color="#2b83ba" label="5"/>
          <item value="34" alpha="255" color="#91cba9" label="34"/>
          <item value="63" alpha="255" color="#def2b4" label="63"/>
          <item value="92" alpha="255" color="#ffdf9a" label="92"/>
          <item value="121" alpha="255" color="#f69053" label="121"/>
          <item value="150" alpha="255" color="#d7191c" label="150"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast brightness="0" contrast="0"/>
    <huesaturation colorizeBlue="128" colorizeStrength="100" colorizeRed="255" grayscaleMode="0" colorizeGreen="128" saturation="0" colorizeOn="0"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>6</blendMode>
</qgis>
