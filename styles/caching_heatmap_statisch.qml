<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" hasScaleBasedVisibilityFlag="0" minScale="1e+08" version="3.10.1-A Coruña" styleCategories="AllStyleCategories">
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
    <rasterrenderer band="1" classificationMax="192" classificationMin="0" alphaBand="-1" opacity="0.754" type="singlebandpseudocolor">
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
        <colorrampshader classificationMode="1" clip="0" colorRampType="INTERPOLATED">
          <colorramp name="[source]" type="gradient">
            <prop v="43,131,186,255" k="color1"/>
            <prop v="215,25,28,255" k="color2"/>
            <prop v="0" k="discrete"/>
            <prop v="gradient" k="rampType"/>
            <prop v="0.25;171,221,164,255:0.5;255,255,191,255:0.75;253,174,97,255" k="stops"/>
          </colorramp>
          <item value="0" alpha="255" color="#2b83ba" label="0"/>
          <item value="48" alpha="255" color="#abdda4" label="48"/>
          <item value="96" alpha="255" color="#ffffbf" label="96"/>
          <item value="144" alpha="255" color="#fdae61" label="144"/>
          <item value="192" alpha="255" color="#d7191c" label="192"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast contrast="0" brightness="0"/>
    <huesaturation colorizeRed="255" colorizeGreen="128" saturation="0" grayscaleMode="0" colorizeStrength="100" colorizeOn="0" colorizeBlue="128"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>6</blendMode>
</qgis>
