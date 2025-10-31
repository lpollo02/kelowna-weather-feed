<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" indent="yes"/>
  <xsl:template match="/">
    <html>
      <head>
        <title>Kelowna Weather RSS</title>
      </head>
      <body>
        <h1>Kelowna Weather RSS Feed</h1>
        <ul>
          <xsl:for-each select="rss/channel/item">
            <li>
              <strong><xsl:value-of select="title"/></strong><br/>
              <xsl:value-of select="description"/>
            </li>
          </xsl:for-each>
        </ul>
      </body>
    </html>
  </xsl:template>
</stylesheet>
