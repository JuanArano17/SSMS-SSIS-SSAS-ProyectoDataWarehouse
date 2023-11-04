import xml.etree.ElementTree as ET

# Tu XML como una cadena (este es un ejemplo con solo 3 registros, pero el concepto es el mismo para 1000 registros)
xml_data = '''<?xml version="1.0" encoding="UTF-8" ?>
<records>
	<record>
		<Customer_PK>1</Customer_PK>
		<Customer_ID>410</Customer_ID>
		<Customer_Name>Olympia Tate</Customer_Name>
		<Customer_Email>dis@google.couk</Customer_Email>
		<Customer_Phone>1-754-627-6524</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-8-20</last_update>
	</record>
	<record>
		<Customer_PK>2</Customer_PK>
		<Customer_ID>101</Customer_ID>
		<Customer_Name>Demetrius Stanley</Customer_Name>
		<Customer_Email>et.commodo@hotmail.edu</Customer_Email>
		<Customer_Phone>1-954-614-4223</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-28</last_update>
	</record>
	<record>
		<Customer_PK>3</Customer_PK>
		<Customer_ID>408</Customer_ID>
		<Customer_Name>Ivy Shields</Customer_Name>
		<Customer_Email>ut@yahoo.com</Customer_Email>
		<Customer_Phone>(246) 434-6261</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-12</last_update>
	</record>
	<record>
		<Customer_PK>4</Customer_PK>
		<Customer_ID>318</Customer_ID>
		<Customer_Name>Phillip Lane</Customer_Name>
		<Customer_Email>dui.lectus@icloud.net</Customer_Email>
		<Customer_Phone>(567) 471-3625</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-23</last_update>
	</record>
	<record>
		<Customer_PK>5</Customer_PK>
		<Customer_ID>272</Customer_ID>
		<Customer_Name>Christine Hewitt</Customer_Name>
		<Customer_Email>sed.diam@outlook.couk</Customer_Email>
		<Customer_Phone>(797) 106-3442</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-4</last_update>
	</record>
	<record>
		<Customer_PK>6</Customer_PK>
		<Customer_ID>47</Customer_ID>
		<Customer_Name>Jescie Lewis</Customer_Name>
		<Customer_Email>urna.nullam@google.net</Customer_Email>
		<Customer_Phone>(432) 721-7112</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-23</last_update>
	</record>
	<record>
		<Customer_PK>7</Customer_PK>
		<Customer_ID>158</Customer_ID>
		<Customer_Name>Iona Rowe</Customer_Name>
		<Customer_Email>mollis@protonmail.ca</Customer_Email>
		<Customer_Phone>(916) 524-2833</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-26</last_update>
	</record>
	<record>
		<Customer_PK>8</Customer_PK>
		<Customer_ID>448</Customer_ID>
		<Customer_Name>Kadeem Puckett</Customer_Name>
		<Customer_Email>malesuada@aol.com</Customer_Email>
		<Customer_Phone>(148) 823-2987</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-15</last_update>
	</record>
	<record>
		<Customer_PK>9</Customer_PK>
		<Customer_ID>92</Customer_ID>
		<Customer_Name>Dominique Riggs</Customer_Name>
		<Customer_Email>mauris@outlook.edu</Customer_Email>
		<Customer_Phone>1-267-901-7122</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-6</last_update>
	</record>
	<record>
		<Customer_PK>10</Customer_PK>
		<Customer_ID>357</Customer_ID>
		<Customer_Name>Selma Day</Customer_Name>
		<Customer_Email>semper.tellus@aol.couk</Customer_Email>
		<Customer_Phone>(815) 643-5019</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-2-9</last_update>
	</record>
	<record>
		<Customer_PK>11</Customer_PK>
		<Customer_ID>163</Customer_ID>
		<Customer_Name>Wyoming Stanton</Customer_Name>
		<Customer_Email>cum.sociis.natoque@yahoo.edu</Customer_Email>
		<Customer_Phone>(687) 237-3339</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-23</last_update>
	</record>
	<record>
		<Customer_PK>12</Customer_PK>
		<Customer_ID>47</Customer_ID>
		<Customer_Name>Laura Hughes</Customer_Name>
		<Customer_Email>magna.a@yahoo.org</Customer_Email>
		<Customer_Phone>1-473-637-8672</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-11-6</last_update>
	</record>
	<record>
		<Customer_PK>13</Customer_PK>
		<Customer_ID>442</Customer_ID>
		<Customer_Name>Penelope Buck</Customer_Name>
		<Customer_Email>in.condimentum.donec@hotmail.edu</Customer_Email>
		<Customer_Phone>(180) 812-3207</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-16</last_update>
	</record>
	<record>
		<Customer_PK>14</Customer_PK>
		<Customer_ID>478</Customer_ID>
		<Customer_Name>Ariel Nixon</Customer_Name>
		<Customer_Email>rhoncus.id.mollis@outlook.org</Customer_Email>
		<Customer_Phone>(651) 872-5596</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-4-22</last_update>
	</record>
	<record>
		<Customer_PK>15</Customer_PK>
		<Customer_ID>301</Customer_ID>
		<Customer_Name>Sybill Bartlett</Customer_Name>
		<Customer_Email>lorem.auctor@protonmail.com</Customer_Email>
		<Customer_Phone>(337) 114-1196</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-29</last_update>
	</record>
	<record>
		<Customer_PK>16</Customer_PK>
		<Customer_ID>4</Customer_ID>
		<Customer_Name>Brody Frost</Customer_Name>
		<Customer_Email>duis.gravida.praesent@aol.ca</Customer_Email>
		<Customer_Phone>1-887-474-7234</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-30</last_update>
	</record>
	<record>
		<Customer_PK>17</Customer_PK>
		<Customer_ID>81</Customer_ID>
		<Customer_Name>Doris Alvarado</Customer_Name>
		<Customer_Email>scelerisque.scelerisque@hotmail.edu</Customer_Email>
		<Customer_Phone>1-185-846-3045</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-1-18</last_update>
	</record>
	<record>
		<Customer_PK>18</Customer_PK>
		<Customer_ID>387</Customer_ID>
		<Customer_Name>Kaseem Richmond</Customer_Name>
		<Customer_Email>tellus.imperdiet@hotmail.net</Customer_Email>
		<Customer_Phone>1-531-163-5717</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-9</last_update>
	</record>
	<record>
		<Customer_PK>19</Customer_PK>
		<Customer_ID>125</Customer_ID>
		<Customer_Name>Keefe Carter</Customer_Name>
		<Customer_Email>vestibulum.lorem@outlook.ca</Customer_Email>
		<Customer_Phone>(617) 489-5320</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-5</last_update>
	</record>
	<record>
		<Customer_PK>20</Customer_PK>
		<Customer_ID>186</Customer_ID>
		<Customer_Name>Maxwell Head</Customer_Name>
		<Customer_Email>mauris.molestie.pharetra@aol.net</Customer_Email>
		<Customer_Phone>1-754-395-7813</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-16</last_update>
	</record>
	<record>
		<Customer_PK>21</Customer_PK>
		<Customer_ID>278</Customer_ID>
		<Customer_Name>Colby Stokes</Customer_Name>
		<Customer_Email>purus.sapien.gravida@google.ca</Customer_Email>
		<Customer_Phone>(684) 782-6447</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-31</last_update>
	</record>
	<record>
		<Customer_PK>22</Customer_PK>
		<Customer_ID>147</Customer_ID>
		<Customer_Name>Axel Wheeler</Customer_Name>
		<Customer_Email>condimentum.donec@outlook.net</Customer_Email>
		<Customer_Phone>1-621-778-4172</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-4-17</last_update>
	</record>
	<record>
		<Customer_PK>23</Customer_PK>
		<Customer_ID>409</Customer_ID>
		<Customer_Name>Darrel Puckett</Customer_Name>
		<Customer_Email>curabitur.massa@aol.couk</Customer_Email>
		<Customer_Phone>1-521-520-8227</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-12</last_update>
	</record>
	<record>
		<Customer_PK>24</Customer_PK>
		<Customer_ID>445</Customer_ID>
		<Customer_Name>Caryn Barrett</Customer_Name>
		<Customer_Email>malesuada.fringilla@outlook.org</Customer_Email>
		<Customer_Phone>(923) 406-7337</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-20</last_update>
	</record>
	<record>
		<Customer_PK>25</Customer_PK>
		<Customer_ID>7</Customer_ID>
		<Customer_Name>Otto Robbins</Customer_Name>
		<Customer_Email>tortor.nunc.commodo@icloud.ca</Customer_Email>
		<Customer_Phone>(213) 411-6271</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-24</last_update>
	</record>
	<record>
		<Customer_PK>26</Customer_PK>
		<Customer_ID>124</Customer_ID>
		<Customer_Name>Karly Head</Customer_Name>
		<Customer_Email>aliquet@yahoo.edu</Customer_Email>
		<Customer_Phone>(546) 436-3445</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-31</last_update>
	</record>
	<record>
		<Customer_PK>27</Customer_PK>
		<Customer_ID>287</Customer_ID>
		<Customer_Name>Bruno James</Customer_Name>
		<Customer_Email>augue.eu.tellus@protonmail.ca</Customer_Email>
		<Customer_Phone>(292) 848-9164</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-15</last_update>
	</record>
	<record>
		<Customer_PK>28</Customer_PK>
		<Customer_ID>281</Customer_ID>
		<Customer_Name>Rashad Bartlett</Customer_Name>
		<Customer_Email>eleifend@protonmail.org</Customer_Email>
		<Customer_Phone>1-403-416-5714</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-9</last_update>
	</record>
	<record>
		<Customer_PK>29</Customer_PK>
		<Customer_ID>293</Customer_ID>
		<Customer_Name>Audrey O'donnell</Customer_Name>
		<Customer_Email>mollis@yahoo.couk</Customer_Email>
		<Customer_Phone>1-943-212-5818</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-12</last_update>
	</record>
	<record>
		<Customer_PK>30</Customer_PK>
		<Customer_ID>80</Customer_ID>
		<Customer_Name>Alan Sullivan</Customer_Name>
		<Customer_Email>elementum.lorem@hotmail.com</Customer_Email>
		<Customer_Phone>(667) 719-6740</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-25</last_update>
	</record>
	<record>
		<Customer_PK>31</Customer_PK>
		<Customer_ID>205</Customer_ID>
		<Customer_Name>Kirsten Mejia</Customer_Name>
		<Customer_Email>dictum.augue@aol.net</Customer_Email>
		<Customer_Phone>1-552-630-8298</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-13</last_update>
	</record>
	<record>
		<Customer_PK>32</Customer_PK>
		<Customer_ID>71</Customer_ID>
		<Customer_Name>Trevor Foster</Customer_Name>
		<Customer_Email>magna@hotmail.couk</Customer_Email>
		<Customer_Phone>1-629-741-3762</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-4-25</last_update>
	</record>
	<record>
		<Customer_PK>33</Customer_PK>
		<Customer_ID>114</Customer_ID>
		<Customer_Name>Nasim Jefferson</Customer_Name>
		<Customer_Email>orci.luctus.et@yahoo.net</Customer_Email>
		<Customer_Phone>(554) 330-6024</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-11-21</last_update>
	</record>
	<record>
		<Customer_PK>34</Customer_PK>
		<Customer_ID>329</Customer_ID>
		<Customer_Name>Donna Herman</Customer_Name>
		<Customer_Email>aliquet.diam.sed@outlook.couk</Customer_Email>
		<Customer_Phone>1-582-565-1165</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-20</last_update>
	</record>
	<record>
		<Customer_PK>35</Customer_PK>
		<Customer_ID>305</Customer_ID>
		<Customer_Name>Eugenia Vang</Customer_Name>
		<Customer_Email>augue.ut@aol.ca</Customer_Email>
		<Customer_Phone>(957) 281-8052</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-29</last_update>
	</record>
	<record>
		<Customer_PK>36</Customer_PK>
		<Customer_ID>352</Customer_ID>
		<Customer_Name>Amaya Hyde</Customer_Name>
		<Customer_Email>nec.ante@yahoo.com</Customer_Email>
		<Customer_Phone>(696) 721-2516</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-1</last_update>
	</record>
	<record>
		<Customer_PK>37</Customer_PK>
		<Customer_ID>374</Customer_ID>
		<Customer_Name>Dylan Price</Customer_Name>
		<Customer_Email>phasellus.dapibus@protonmail.net</Customer_Email>
		<Customer_Phone>1-871-986-1718</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-13</last_update>
	</record>
	<record>
		<Customer_PK>38</Customer_PK>
		<Customer_ID>29</Customer_ID>
		<Customer_Name>Kitra Hall</Customer_Name>
		<Customer_Email>proin.eget@yahoo.edu</Customer_Email>
		<Customer_Phone>(230) 534-8167</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-8-22</last_update>
	</record>
	<record>
		<Customer_PK>39</Customer_PK>
		<Customer_ID>243</Customer_ID>
		<Customer_Name>Heather Hays</Customer_Name>
		<Customer_Email>ultrices.duis.volutpat@yahoo.org</Customer_Email>
		<Customer_Phone>(428) 502-0615</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-4-2</last_update>
	</record>
	<record>
		<Customer_PK>40</Customer_PK>
		<Customer_ID>338</Customer_ID>
		<Customer_Name>Anjolie Haynes</Customer_Name>
		<Customer_Email>ut.eros@outlook.couk</Customer_Email>
		<Customer_Phone>(684) 330-7383</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-13</last_update>
	</record>
	<record>
		<Customer_PK>41</Customer_PK>
		<Customer_ID>425</Customer_ID>
		<Customer_Name>Constance Hewitt</Customer_Name>
		<Customer_Email>metus@google.net</Customer_Email>
		<Customer_Phone>1-556-970-9084</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-8-13</last_update>
	</record>
	<record>
		<Customer_PK>42</Customer_PK>
		<Customer_ID>26</Customer_ID>
		<Customer_Name>Warren Blackwell</Customer_Name>
		<Customer_Email>sem.pellentesque@protonmail.couk</Customer_Email>
		<Customer_Phone>1-885-757-3311</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-2</last_update>
	</record>
	<record>
		<Customer_PK>43</Customer_PK>
		<Customer_ID>39</Customer_ID>
		<Customer_Name>Stuart Dodson</Customer_Name>
		<Customer_Email>id.sapien.cras@google.couk</Customer_Email>
		<Customer_Phone>(340) 250-4399</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-15</last_update>
	</record>
	<record>
		<Customer_PK>44</Customer_PK>
		<Customer_ID>3</Customer_ID>
		<Customer_Name>Lee Goodman</Customer_Name>
		<Customer_Email>sit.amet@aol.edu</Customer_Email>
		<Customer_Phone>1-811-401-1003</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-17</last_update>
	</record>
	<record>
		<Customer_PK>45</Customer_PK>
		<Customer_ID>373</Customer_ID>
		<Customer_Name>Harrison Byrd</Customer_Name>
		<Customer_Email>purus.nullam@protonmail.edu</Customer_Email>
		<Customer_Phone>1-993-798-3155</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-8</last_update>
	</record>
	<record>
		<Customer_PK>46</Customer_PK>
		<Customer_ID>160</Customer_ID>
		<Customer_Name>Trevor Randolph</Customer_Name>
		<Customer_Email>est.mauris@hotmail.ca</Customer_Email>
		<Customer_Phone>(644) 799-7614</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-9-5</last_update>
	</record>
	<record>
		<Customer_PK>47</Customer_PK>
		<Customer_ID>469</Customer_ID>
		<Customer_Name>Kasimir Dillard</Customer_Name>
		<Customer_Email>lorem.luctus@icloud.edu</Customer_Email>
		<Customer_Phone>(835) 825-4657</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-20</last_update>
	</record>
	<record>
		<Customer_PK>48</Customer_PK>
		<Customer_ID>321</Customer_ID>
		<Customer_Name>Summer Haney</Customer_Name>
		<Customer_Email>mauris.erat@protonmail.org</Customer_Email>
		<Customer_Phone>(678) 653-7729</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-19</last_update>
	</record>
	<record>
		<Customer_PK>49</Customer_PK>
		<Customer_ID>460</Customer_ID>
		<Customer_Name>Phelan Parrish</Customer_Name>
		<Customer_Email>quisque@yahoo.net</Customer_Email>
		<Customer_Phone>(373) 230-8418</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-5-13</last_update>
	</record>
	<record>
		<Customer_PK>50</Customer_PK>
		<Customer_ID>101</Customer_ID>
		<Customer_Name>Maxine Parker</Customer_Name>
		<Customer_Email>lorem.tristique.aliquet@yahoo.edu</Customer_Email>
		<Customer_Phone>1-846-735-0013</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-20</last_update>
	</record>
	<record>
		<Customer_PK>51</Customer_PK>
		<Customer_ID>184</Customer_ID>
		<Customer_Name>Maris Palmer</Customer_Name>
		<Customer_Email>lectus.pede@aol.com</Customer_Email>
		<Customer_Phone>1-374-828-4187</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-4</last_update>
	</record>
	<record>
		<Customer_PK>52</Customer_PK>
		<Customer_ID>329</Customer_ID>
		<Customer_Name>Ferris Whitley</Customer_Name>
		<Customer_Email>sagittis@protonmail.net</Customer_Email>
		<Customer_Phone>1-804-557-0876</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-27</last_update>
	</record>
	<record>
		<Customer_PK>53</Customer_PK>
		<Customer_ID>310</Customer_ID>
		<Customer_Name>Brenden Burks</Customer_Name>
		<Customer_Email>diam@outlook.edu</Customer_Email>
		<Customer_Phone>1-432-342-1962</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-24</last_update>
	</record>
	<record>
		<Customer_PK>54</Customer_PK>
		<Customer_ID>324</Customer_ID>
		<Customer_Name>Brady Hill</Customer_Name>
		<Customer_Email>mi.duis@aol.edu</Customer_Email>
		<Customer_Phone>(356) 770-4670</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-19</last_update>
	</record>
	<record>
		<Customer_PK>55</Customer_PK>
		<Customer_ID>154</Customer_ID>
		<Customer_Name>Lucian Battle</Customer_Name>
		<Customer_Email>urna@google.com</Customer_Email>
		<Customer_Phone>1-670-474-2750</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-31</last_update>
	</record>
	<record>
		<Customer_PK>56</Customer_PK>
		<Customer_ID>361</Customer_ID>
		<Customer_Name>Paul Sandoval</Customer_Name>
		<Customer_Email>ultricies.dignissim@hotmail.net</Customer_Email>
		<Customer_Phone>1-482-798-5731</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-22</last_update>
	</record>
	<record>
		<Customer_PK>57</Customer_PK>
		<Customer_ID>99</Customer_ID>
		<Customer_Name>Shellie Gordon</Customer_Name>
		<Customer_Email>nulla.integer@outlook.ca</Customer_Email>
		<Customer_Phone>(588) 211-4820</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-19</last_update>
	</record>
	<record>
		<Customer_PK>58</Customer_PK>
		<Customer_ID>94</Customer_ID>
		<Customer_Name>Aurora Garner</Customer_Name>
		<Customer_Email>ullamcorper.eu@protonmail.couk</Customer_Email>
		<Customer_Phone>(374) 357-6665</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-12</last_update>
	</record>
	<record>
		<Customer_PK>59</Customer_PK>
		<Customer_ID>19</Customer_ID>
		<Customer_Name>Raja Golden</Customer_Name>
		<Customer_Email>morbi.vehicula@google.ca</Customer_Email>
		<Customer_Phone>1-426-342-0249</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-8-25</last_update>
	</record>
	<record>
		<Customer_PK>60</Customer_PK>
		<Customer_ID>450</Customer_ID>
		<Customer_Name>Mannix Weber</Customer_Name>
		<Customer_Email>est.mauris@outlook.edu</Customer_Email>
		<Customer_Phone>1-173-490-3037</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-14</last_update>
	</record>
	<record>
		<Customer_PK>61</Customer_PK>
		<Customer_ID>377</Customer_ID>
		<Customer_Name>Sylvester Ortega</Customer_Name>
		<Customer_Email>sapien.cras@aol.ca</Customer_Email>
		<Customer_Phone>(301) 721-1325</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-18</last_update>
	</record>
	<record>
		<Customer_PK>62</Customer_PK>
		<Customer_ID>332</Customer_ID>
		<Customer_Name>Madeline Butler</Customer_Name>
		<Customer_Email>at@hotmail.net</Customer_Email>
		<Customer_Phone>1-894-643-1543</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-23</last_update>
	</record>
	<record>
		<Customer_PK>63</Customer_PK>
		<Customer_ID>451</Customer_ID>
		<Customer_Name>Iliana Newman</Customer_Name>
		<Customer_Email>leo@icloud.com</Customer_Email>
		<Customer_Phone>(568) 719-7818</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-24</last_update>
	</record>
	<record>
		<Customer_PK>64</Customer_PK>
		<Customer_ID>337</Customer_ID>
		<Customer_Name>Barclay Alvarez</Customer_Name>
		<Customer_Email>sit.amet@yahoo.ca</Customer_Email>
		<Customer_Phone>1-367-331-7328</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-4-27</last_update>
	</record>
	<record>
		<Customer_PK>65</Customer_PK>
		<Customer_ID>135</Customer_ID>
		<Customer_Name>Pascale Benson</Customer_Name>
		<Customer_Email>gravida.aliquam@outlook.net</Customer_Email>
		<Customer_Phone>(216) 151-2181</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-2</last_update>
	</record>
	<record>
		<Customer_PK>66</Customer_PK>
		<Customer_ID>468</Customer_ID>
		<Customer_Name>Nola Burch</Customer_Name>
		<Customer_Email>lacus.mauris@aol.couk</Customer_Email>
		<Customer_Phone>(334) 755-9733</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-14</last_update>
	</record>
	<record>
		<Customer_PK>67</Customer_PK>
		<Customer_ID>471</Customer_ID>
		<Customer_Name>Ava Burgess</Customer_Name>
		<Customer_Email>cras.lorem@icloud.org</Customer_Email>
		<Customer_Phone>1-352-743-8392</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-12</last_update>
	</record>
	<record>
		<Customer_PK>68</Customer_PK>
		<Customer_ID>117</Customer_ID>
		<Customer_Name>Chadwick Padilla</Customer_Name>
		<Customer_Email>rutrum.fusce@hotmail.net</Customer_Email>
		<Customer_Phone>(860) 544-9253</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-15</last_update>
	</record>
	<record>
		<Customer_PK>69</Customer_PK>
		<Customer_ID>81</Customer_ID>
		<Customer_Name>Patricia Mcfadden</Customer_Name>
		<Customer_Email>adipiscing.non.luctus@aol.ca</Customer_Email>
		<Customer_Phone>(228) 156-2264</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-6</last_update>
	</record>
	<record>
		<Customer_PK>70</Customer_PK>
		<Customer_ID>82</Customer_ID>
		<Customer_Name>Erasmus Hahn</Customer_Name>
		<Customer_Email>enim@protonmail.com</Customer_Email>
		<Customer_Phone>1-445-695-3318</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-11-15</last_update>
	</record>
	<record>
		<Customer_PK>71</Customer_PK>
		<Customer_ID>189</Customer_ID>
		<Customer_Name>Aiko Harmon</Customer_Name>
		<Customer_Email>nisi.a@aol.org</Customer_Email>
		<Customer_Phone>(452) 361-0765</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-1</last_update>
	</record>
	<record>
		<Customer_PK>72</Customer_PK>
		<Customer_ID>259</Customer_ID>
		<Customer_Name>Shelly Walter</Customer_Name>
		<Customer_Email>euismod.enim@yahoo.org</Customer_Email>
		<Customer_Phone>1-365-715-4727</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-15</last_update>
	</record>
	<record>
		<Customer_PK>73</Customer_PK>
		<Customer_ID>154</Customer_ID>
		<Customer_Name>Faith Moody</Customer_Name>
		<Customer_Email>natoque.penatibus@icloud.ca</Customer_Email>
		<Customer_Phone>(268) 730-0567</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-1-12</last_update>
	</record>
	<record>
		<Customer_PK>74</Customer_PK>
		<Customer_ID>475</Customer_ID>
		<Customer_Name>Allen Kemp</Customer_Name>
		<Customer_Email>ut.mi@yahoo.org</Customer_Email>
		<Customer_Phone>1-952-215-8412</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-15</last_update>
	</record>
	<record>
		<Customer_PK>75</Customer_PK>
		<Customer_ID>186</Customer_ID>
		<Customer_Name>Melanie Diaz</Customer_Name>
		<Customer_Email>pede.ultrices@aol.net</Customer_Email>
		<Customer_Phone>(781) 481-7105</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-19</last_update>
	</record>
	<record>
		<Customer_PK>76</Customer_PK>
		<Customer_ID>360</Customer_ID>
		<Customer_Name>Otto Boyle</Customer_Name>
		<Customer_Email>egestas@protonmail.ca</Customer_Email>
		<Customer_Phone>(621) 423-1516</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-4</last_update>
	</record>
	<record>
		<Customer_PK>77</Customer_PK>
		<Customer_ID>86</Customer_ID>
		<Customer_Name>Amanda Mcguire</Customer_Name>
		<Customer_Email>rhoncus@aol.edu</Customer_Email>
		<Customer_Phone>(688) 236-3653</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-11-25</last_update>
	</record>
	<record>
		<Customer_PK>78</Customer_PK>
		<Customer_ID>95</Customer_ID>
		<Customer_Name>Maya Hubbard</Customer_Name>
		<Customer_Email>ante.bibendum.ullamcorper@aol.couk</Customer_Email>
		<Customer_Phone>1-246-483-4573</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-16</last_update>
	</record>
	<record>
		<Customer_PK>79</Customer_PK>
		<Customer_ID>112</Customer_ID>
		<Customer_Name>Melvin Patton</Customer_Name>
		<Customer_Email>erat.vivamus@yahoo.couk</Customer_Email>
		<Customer_Phone>(322) 426-3821</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-29</last_update>
	</record>
	<record>
		<Customer_PK>80</Customer_PK>
		<Customer_ID>489</Customer_ID>
		<Customer_Name>Xandra Caldwell</Customer_Name>
		<Customer_Email>sit@outlook.edu</Customer_Email>
		<Customer_Phone>1-269-527-8467</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-8</last_update>
	</record>
	<record>
		<Customer_PK>81</Customer_PK>
		<Customer_ID>218</Customer_ID>
		<Customer_Name>Gwendolyn Cantrell</Customer_Name>
		<Customer_Email>diam.pellentesque@outlook.net</Customer_Email>
		<Customer_Phone>1-128-898-1843</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-20</last_update>
	</record>
	<record>
		<Customer_PK>82</Customer_PK>
		<Customer_ID>430</Customer_ID>
		<Customer_Name>Beau Kelley</Customer_Name>
		<Customer_Email>fusce.diam@yahoo.net</Customer_Email>
		<Customer_Phone>(458) 578-7875</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-11-21</last_update>
	</record>
	<record>
		<Customer_PK>83</Customer_PK>
		<Customer_ID>497</Customer_ID>
		<Customer_Name>Edward Murray</Customer_Name>
		<Customer_Email>iaculis@hotmail.net</Customer_Email>
		<Customer_Phone>(933) 529-4285</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-2</last_update>
	</record>
	<record>
		<Customer_PK>84</Customer_PK>
		<Customer_ID>46</Customer_ID>
		<Customer_Name>Finn Landry</Customer_Name>
		<Customer_Email>commodo@icloud.com</Customer_Email>
		<Customer_Phone>(937) 586-5159</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-2-16</last_update>
	</record>
	<record>
		<Customer_PK>85</Customer_PK>
		<Customer_ID>315</Customer_ID>
		<Customer_Name>Illiana Mendoza</Customer_Name>
		<Customer_Email>blandit.congue.in@outlook.net</Customer_Email>
		<Customer_Phone>1-743-773-0367</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-8-31</last_update>
	</record>
	<record>
		<Customer_PK>86</Customer_PK>
		<Customer_ID>33</Customer_ID>
		<Customer_Name>Yoshio Grimes</Customer_Name>
		<Customer_Email>vitae.posuere@aol.edu</Customer_Email>
		<Customer_Phone>1-737-833-6500</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-11</last_update>
	</record>
	<record>
		<Customer_PK>87</Customer_PK>
		<Customer_ID>301</Customer_ID>
		<Customer_Name>Addison Cleveland</Customer_Name>
		<Customer_Email>ornare.elit@yahoo.org</Customer_Email>
		<Customer_Phone>1-761-653-8072</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-26</last_update>
	</record>
	<record>
		<Customer_PK>88</Customer_PK>
		<Customer_ID>496</Customer_ID>
		<Customer_Name>Dale Horn</Customer_Name>
		<Customer_Email>porttitor.eros@protonmail.couk</Customer_Email>
		<Customer_Phone>1-996-283-5432</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-8-8</last_update>
	</record>
	<record>
		<Customer_PK>89</Customer_PK>
		<Customer_ID>406</Customer_ID>
		<Customer_Name>Kessie Burris</Customer_Name>
		<Customer_Email>morbi@yahoo.ca</Customer_Email>
		<Customer_Phone>1-826-585-2341</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-7</last_update>
	</record>
	<record>
		<Customer_PK>90</Customer_PK>
		<Customer_ID>308</Customer_ID>
		<Customer_Name>Delilah Vincent</Customer_Name>
		<Customer_Email>lectus.a@hotmail.ca</Customer_Email>
		<Customer_Phone>1-472-372-4506</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-10</last_update>
	</record>
	<record>
		<Customer_PK>91</Customer_PK>
		<Customer_ID>374</Customer_ID>
		<Customer_Name>Xyla Massey</Customer_Name>
		<Customer_Email>luctus.et.ultrices@aol.couk</Customer_Email>
		<Customer_Phone>1-161-558-1491</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-2</last_update>
	</record>
	<record>
		<Customer_PK>92</Customer_PK>
		<Customer_ID>451</Customer_ID>
		<Customer_Name>Inga Haney</Customer_Name>
		<Customer_Email>nibh.aliquam@outlook.net</Customer_Email>
		<Customer_Phone>1-364-730-4182</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-20</last_update>
	</record>
	<record>
		<Customer_PK>93</Customer_PK>
		<Customer_ID>137</Customer_ID>
		<Customer_Name>Kelsey Rice</Customer_Name>
		<Customer_Email>nam@aol.net</Customer_Email>
		<Customer_Phone>(843) 756-6877</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-13</last_update>
	</record>
	<record>
		<Customer_PK>94</Customer_PK>
		<Customer_ID>61</Customer_ID>
		<Customer_Name>Rhonda Clark</Customer_Name>
		<Customer_Email>etiam.ligula@icloud.edu</Customer_Email>
		<Customer_Phone>(464) 853-1874</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-8</last_update>
	</record>
	<record>
		<Customer_PK>95</Customer_PK>
		<Customer_ID>457</Customer_ID>
		<Customer_Name>Rae Cochran</Customer_Name>
		<Customer_Email>sapien.imperdiet@protonmail.edu</Customer_Email>
		<Customer_Phone>(794) 822-7360</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-6</last_update>
	</record>
	<record>
		<Customer_PK>96</Customer_PK>
		<Customer_ID>229</Customer_ID>
		<Customer_Name>Abdul Cox</Customer_Name>
		<Customer_Email>justo.praesent@yahoo.couk</Customer_Email>
		<Customer_Phone>1-675-442-1375</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-7</last_update>
	</record>
	<record>
		<Customer_PK>97</Customer_PK>
		<Customer_ID>251</Customer_ID>
		<Customer_Name>Ella Flores</Customer_Name>
		<Customer_Email>est.tempor@hotmail.ca</Customer_Email>
		<Customer_Phone>1-780-327-5293</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-28</last_update>
	</record>
	<record>
		<Customer_PK>98</Customer_PK>
		<Customer_ID>340</Customer_ID>
		<Customer_Name>Yvette Pena</Customer_Name>
		<Customer_Email>cursus.et@aol.org</Customer_Email>
		<Customer_Phone>1-294-558-0334</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-21</last_update>
	</record>
	<record>
		<Customer_PK>99</Customer_PK>
		<Customer_ID>139</Customer_ID>
		<Customer_Name>Uriel Gentry</Customer_Name>
		<Customer_Email>vulputate.lacus@outlook.ca</Customer_Email>
		<Customer_Phone>(455) 738-2142</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-11</last_update>
	</record>
	<record>
		<Customer_PK>100</Customer_PK>
		<Customer_ID>251</Customer_ID>
		<Customer_Name>Addison Nichols</Customer_Name>
		<Customer_Email>sem.pellentesque@aol.net</Customer_Email>
		<Customer_Phone>1-868-718-3552</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-5</last_update>
	</record>
	<record>
		<Customer_PK>101</Customer_PK>
		<Customer_ID>257</Customer_ID>
		<Customer_Name>Shana Lee</Customer_Name>
		<Customer_Email>id.enim@hotmail.edu</Customer_Email>
		<Customer_Phone>1-260-239-3184</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-29</last_update>
	</record>
	<record>
		<Customer_PK>102</Customer_PK>
		<Customer_ID>279</Customer_ID>
		<Customer_Name>Akeem Hunter</Customer_Name>
		<Customer_Email>nisi.a@icloud.net</Customer_Email>
		<Customer_Phone>(754) 974-1376</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-12</last_update>
	</record>
	<record>
		<Customer_PK>103</Customer_PK>
		<Customer_ID>197</Customer_ID>
		<Customer_Name>Quinn Mcleod</Customer_Name>
		<Customer_Email>tempus.risus@google.net</Customer_Email>
		<Customer_Phone>1-469-374-2735</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-22</last_update>
	</record>
	<record>
		<Customer_PK>104</Customer_PK>
		<Customer_ID>159</Customer_ID>
		<Customer_Name>Jin Stevens</Customer_Name>
		<Customer_Email>eget.dictum@icloud.com</Customer_Email>
		<Customer_Phone>(942) 114-3714</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-20</last_update>
	</record>
	<record>
		<Customer_PK>105</Customer_PK>
		<Customer_ID>95</Customer_ID>
		<Customer_Name>Vernon Merrill</Customer_Name>
		<Customer_Email>lorem@protonmail.couk</Customer_Email>
		<Customer_Phone>(211) 221-4122</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-13</last_update>
	</record>
	<record>
		<Customer_PK>106</Customer_PK>
		<Customer_ID>410</Customer_ID>
		<Customer_Name>Whitney Hendrix</Customer_Name>
		<Customer_Email>dapibus@google.edu</Customer_Email>
		<Customer_Phone>1-883-689-6340</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-19</last_update>
	</record>
	<record>
		<Customer_PK>107</Customer_PK>
		<Customer_ID>371</Customer_ID>
		<Customer_Name>Palmer Griffith</Customer_Name>
		<Customer_Email>tempor.bibendum.donec@hotmail.net</Customer_Email>
		<Customer_Phone>(728) 267-2210</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-31</last_update>
	</record>
	<record>
		<Customer_PK>108</Customer_PK>
		<Customer_ID>263</Customer_ID>
		<Customer_Name>Simone Shields</Customer_Name>
		<Customer_Email>luctus.sit@yahoo.edu</Customer_Email>
		<Customer_Phone>(588) 203-1965</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-17</last_update>
	</record>
	<record>
		<Customer_PK>109</Customer_PK>
		<Customer_ID>181</Customer_ID>
		<Customer_Name>Chadwick Fuentes</Customer_Name>
		<Customer_Email>ullamcorper.velit@protonmail.com</Customer_Email>
		<Customer_Phone>1-652-601-3022</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-16</last_update>
	</record>
	<record>
		<Customer_PK>110</Customer_PK>
		<Customer_ID>285</Customer_ID>
		<Customer_Name>Chaney Guerrero</Customer_Name>
		<Customer_Email>mauris.blandit.enim@yahoo.edu</Customer_Email>
		<Customer_Phone>(322) 266-1834</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-12</last_update>
	</record>
	<record>
		<Customer_PK>111</Customer_PK>
		<Customer_ID>353</Customer_ID>
		<Customer_Name>Tamara O'Neill</Customer_Name>
		<Customer_Email>velit@icloud.couk</Customer_Email>
		<Customer_Phone>1-488-187-2556</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-23</last_update>
	</record>
	<record>
		<Customer_PK>112</Customer_PK>
		<Customer_ID>397</Customer_ID>
		<Customer_Name>Indigo West</Customer_Name>
		<Customer_Email>fermentum.fermentum@yahoo.couk</Customer_Email>
		<Customer_Phone>1-529-239-7064</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-11-10</last_update>
	</record>
	<record>
		<Customer_PK>113</Customer_PK>
		<Customer_ID>39</Customer_ID>
		<Customer_Name>Kirby Pickett</Customer_Name>
		<Customer_Email>ligula.elit@aol.edu</Customer_Email>
		<Customer_Phone>(688) 363-7870</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-11</last_update>
	</record>
	<record>
		<Customer_PK>114</Customer_PK>
		<Customer_ID>267</Customer_ID>
		<Customer_Name>Zephania Rodriguez</Customer_Name>
		<Customer_Email>elit.elit.fermentum@protonmail.ca</Customer_Email>
		<Customer_Phone>(756) 873-7235</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-24</last_update>
	</record>
	<record>
		<Customer_PK>115</Customer_PK>
		<Customer_ID>138</Customer_ID>
		<Customer_Name>Zane Perkins</Customer_Name>
		<Customer_Email>massa.non@icloud.ca</Customer_Email>
		<Customer_Phone>(356) 747-7836</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-11</last_update>
	</record>
	<record>
		<Customer_PK>116</Customer_PK>
		<Customer_ID>63</Customer_ID>
		<Customer_Name>Rigel Watkins</Customer_Name>
		<Customer_Email>ornare.elit@outlook.org</Customer_Email>
		<Customer_Phone>(235) 856-2280</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-2</last_update>
	</record>
	<record>
		<Customer_PK>117</Customer_PK>
		<Customer_ID>379</Customer_ID>
		<Customer_Name>Dillon Parks</Customer_Name>
		<Customer_Email>ultrices.a@protonmail.com</Customer_Email>
		<Customer_Phone>1-577-544-9656</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-5-30</last_update>
	</record>
	<record>
		<Customer_PK>118</Customer_PK>
		<Customer_ID>263</Customer_ID>
		<Customer_Name>Dillon Watkins</Customer_Name>
		<Customer_Email>velit.justo.nec@icloud.ca</Customer_Email>
		<Customer_Phone>(267) 239-2552</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-24</last_update>
	</record>
	<record>
		<Customer_PK>119</Customer_PK>
		<Customer_ID>306</Customer_ID>
		<Customer_Name>Xavier Kemp</Customer_Name>
		<Customer_Email>ipsum.suspendisse@yahoo.net</Customer_Email>
		<Customer_Phone>(632) 665-3543</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-9-10</last_update>
	</record>
	<record>
		<Customer_PK>120</Customer_PK>
		<Customer_ID>241</Customer_ID>
		<Customer_Name>Hannah Steele</Customer_Name>
		<Customer_Email>in.molestie.tortor@outlook.ca</Customer_Email>
		<Customer_Phone>1-322-328-5454</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-6</last_update>
	</record>
	<record>
		<Customer_PK>121</Customer_PK>
		<Customer_ID>356</Customer_ID>
		<Customer_Name>Price Chase</Customer_Name>
		<Customer_Email>integer.sem@yahoo.ca</Customer_Email>
		<Customer_Phone>1-824-492-7483</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-8-13</last_update>
	</record>
	<record>
		<Customer_PK>122</Customer_PK>
		<Customer_ID>116</Customer_ID>
		<Customer_Name>Philip Haley</Customer_Name>
		<Customer_Email>interdum@outlook.com</Customer_Email>
		<Customer_Phone>1-653-614-5234</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-11-25</last_update>
	</record>
	<record>
		<Customer_PK>123</Customer_PK>
		<Customer_ID>142</Customer_ID>
		<Customer_Name>Heather Mcclure</Customer_Name>
		<Customer_Email>odio.a@yahoo.couk</Customer_Email>
		<Customer_Phone>1-526-241-7312</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-2-22</last_update>
	</record>
	<record>
		<Customer_PK>124</Customer_PK>
		<Customer_ID>206</Customer_ID>
		<Customer_Name>Barrett Robinson</Customer_Name>
		<Customer_Email>lacinia@outlook.couk</Customer_Email>
		<Customer_Phone>1-566-709-8831</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-10</last_update>
	</record>
	<record>
		<Customer_PK>125</Customer_PK>
		<Customer_ID>118</Customer_ID>
		<Customer_Name>Nita Reese</Customer_Name>
		<Customer_Email>in.sodales.elit@google.edu</Customer_Email>
		<Customer_Phone>(488) 866-8542</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-12</last_update>
	</record>
	<record>
		<Customer_PK>126</Customer_PK>
		<Customer_ID>23</Customer_ID>
		<Customer_Name>Cynthia Orr</Customer_Name>
		<Customer_Email>eu@protonmail.com</Customer_Email>
		<Customer_Phone>1-622-432-7125</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-8-10</last_update>
	</record>
	<record>
		<Customer_PK>127</Customer_PK>
		<Customer_ID>239</Customer_ID>
		<Customer_Name>Ruth Henson</Customer_Name>
		<Customer_Email>amet.ornare@hotmail.net</Customer_Email>
		<Customer_Phone>1-205-187-7783</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-30</last_update>
	</record>
	<record>
		<Customer_PK>128</Customer_PK>
		<Customer_ID>371</Customer_ID>
		<Customer_Name>Sean Stuart</Customer_Name>
		<Customer_Email>integer.tincidunt@aol.org</Customer_Email>
		<Customer_Phone>(421) 318-7265</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-4-21</last_update>
	</record>
	<record>
		<Customer_PK>129</Customer_PK>
		<Customer_ID>56</Customer_ID>
		<Customer_Name>Herman Decker</Customer_Name>
		<Customer_Email>fringilla.est.mauris@outlook.edu</Customer_Email>
		<Customer_Phone>(852) 227-0766</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-18</last_update>
	</record>
	<record>
		<Customer_PK>130</Customer_PK>
		<Customer_ID>91</Customer_ID>
		<Customer_Name>Madonna Leach</Customer_Name>
		<Customer_Email>facilisis@outlook.org</Customer_Email>
		<Customer_Phone>(683) 571-0382</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-15</last_update>
	</record>
	<record>
		<Customer_PK>131</Customer_PK>
		<Customer_ID>318</Customer_ID>
		<Customer_Name>Martha Price</Customer_Name>
		<Customer_Email>nisl.arcu.iaculis@icloud.ca</Customer_Email>
		<Customer_Phone>1-459-353-8261</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-6</last_update>
	</record>
	<record>
		<Customer_PK>132</Customer_PK>
		<Customer_ID>184</Customer_ID>
		<Customer_Name>Sylvester Buckley</Customer_Name>
		<Customer_Email>urna.convallis@hotmail.net</Customer_Email>
		<Customer_Phone>1-730-466-4706</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-8-19</last_update>
	</record>
	<record>
		<Customer_PK>133</Customer_PK>
		<Customer_ID>288</Customer_ID>
		<Customer_Name>Bruce Kirby</Customer_Name>
		<Customer_Email>et.magnis@yahoo.edu</Customer_Email>
		<Customer_Phone>(468) 477-7845</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-2</last_update>
	</record>
	<record>
		<Customer_PK>134</Customer_PK>
		<Customer_ID>21</Customer_ID>
		<Customer_Name>Lee Bradshaw</Customer_Name>
		<Customer_Email>elit.nulla.facilisi@google.edu</Customer_Email>
		<Customer_Phone>(235) 736-6866</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-6</last_update>
	</record>
	<record>
		<Customer_PK>135</Customer_PK>
		<Customer_ID>364</Customer_ID>
		<Customer_Name>Melodie Gates</Customer_Name>
		<Customer_Email>dis@icloud.edu</Customer_Email>
		<Customer_Phone>1-346-851-9825</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-14</last_update>
	</record>
	<record>
		<Customer_PK>136</Customer_PK>
		<Customer_ID>422</Customer_ID>
		<Customer_Name>Jelani Hays</Customer_Name>
		<Customer_Email>integer.in@protonmail.edu</Customer_Email>
		<Customer_Phone>1-257-964-6750</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-22</last_update>
	</record>
	<record>
		<Customer_PK>137</Customer_PK>
		<Customer_ID>470</Customer_ID>
		<Customer_Name>Quinlan Arnold</Customer_Name>
		<Customer_Email>magnis.dis@google.edu</Customer_Email>
		<Customer_Phone>1-219-845-9141</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-4</last_update>
	</record>
	<record>
		<Customer_PK>138</Customer_PK>
		<Customer_ID>234</Customer_ID>
		<Customer_Name>Nasim Guerra</Customer_Name>
		<Customer_Email>convallis@yahoo.com</Customer_Email>
		<Customer_Phone>1-962-381-5438</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-11</last_update>
	</record>
	<record>
		<Customer_PK>139</Customer_PK>
		<Customer_ID>97</Customer_ID>
		<Customer_Name>Kamal Gilliam</Customer_Name>
		<Customer_Email>proin@protonmail.net</Customer_Email>
		<Customer_Phone>1-245-295-8438</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-1</last_update>
	</record>
	<record>
		<Customer_PK>140</Customer_PK>
		<Customer_ID>488</Customer_ID>
		<Customer_Name>Ima Reilly</Customer_Name>
		<Customer_Email>mauris.blandit.enim@outlook.net</Customer_Email>
		<Customer_Phone>1-261-858-1876</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-5-18</last_update>
	</record>
	<record>
		<Customer_PK>141</Customer_PK>
		<Customer_ID>328</Customer_ID>
		<Customer_Name>Colette Murray</Customer_Name>
		<Customer_Email>mi.duis@google.couk</Customer_Email>
		<Customer_Phone>1-867-567-4491</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-27</last_update>
	</record>
	<record>
		<Customer_PK>142</Customer_PK>
		<Customer_ID>275</Customer_ID>
		<Customer_Name>Madonna Jarvis</Customer_Name>
		<Customer_Email>sit@protonmail.com</Customer_Email>
		<Customer_Phone>1-221-234-5662</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-26</last_update>
	</record>
	<record>
		<Customer_PK>143</Customer_PK>
		<Customer_ID>374</Customer_ID>
		<Customer_Name>Rhonda Sutton</Customer_Name>
		<Customer_Email>accumsan@outlook.ca</Customer_Email>
		<Customer_Phone>(882) 605-9879</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-10-25</last_update>
	</record>
	<record>
		<Customer_PK>144</Customer_PK>
		<Customer_ID>60</Customer_ID>
		<Customer_Name>Wyatt Scott</Customer_Name>
		<Customer_Email>quisque.purus.sapien@yahoo.com</Customer_Email>
		<Customer_Phone>1-238-212-3132</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-24</last_update>
	</record>
	<record>
		<Customer_PK>145</Customer_PK>
		<Customer_ID>97</Customer_ID>
		<Customer_Name>Ivana Nichols</Customer_Name>
		<Customer_Email>sollicitudin.a.malesuada@google.org</Customer_Email>
		<Customer_Phone>1-869-788-6541</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-8-22</last_update>
	</record>
	<record>
		<Customer_PK>146</Customer_PK>
		<Customer_ID>42</Customer_ID>
		<Customer_Name>Cassidy Shaw</Customer_Name>
		<Customer_Email>tempor.erat@google.net</Customer_Email>
		<Customer_Phone>(461) 626-7381</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-19</last_update>
	</record>
	<record>
		<Customer_PK>147</Customer_PK>
		<Customer_ID>100</Customer_ID>
		<Customer_Name>Oleg Lancaster</Customer_Name>
		<Customer_Email>est@yahoo.edu</Customer_Email>
		<Customer_Phone>1-713-931-7865</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-1</last_update>
	</record>
	<record>
		<Customer_PK>148</Customer_PK>
		<Customer_ID>177</Customer_ID>
		<Customer_Name>Howard Blake</Customer_Name>
		<Customer_Email>in.felis@icloud.couk</Customer_Email>
		<Customer_Phone>(811) 774-3634</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-19</last_update>
	</record>
	<record>
		<Customer_PK>149</Customer_PK>
		<Customer_ID>245</Customer_ID>
		<Customer_Name>Hadley Bates</Customer_Name>
		<Customer_Email>vitae.mauris.sit@hotmail.couk</Customer_Email>
		<Customer_Phone>1-308-700-9282</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-9-29</last_update>
	</record>
	<record>
		<Customer_PK>150</Customer_PK>
		<Customer_ID>35</Customer_ID>
		<Customer_Name>Hakeem Houston</Customer_Name>
		<Customer_Email>dapibus.gravida.aliquam@protonmail.net</Customer_Email>
		<Customer_Phone>1-623-587-3545</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-4-3</last_update>
	</record>
	<record>
		<Customer_PK>151</Customer_PK>
		<Customer_ID>369</Customer_ID>
		<Customer_Name>Hanae Hartman</Customer_Name>
		<Customer_Email>faucibus.morbi@hotmail.com</Customer_Email>
		<Customer_Phone>1-547-962-6782</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-18</last_update>
	</record>
	<record>
		<Customer_PK>152</Customer_PK>
		<Customer_ID>193</Customer_ID>
		<Customer_Name>Beau Buchanan</Customer_Name>
		<Customer_Email>est.congue@hotmail.org</Customer_Email>
		<Customer_Phone>(665) 369-6007</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-19</last_update>
	</record>
	<record>
		<Customer_PK>153</Customer_PK>
		<Customer_ID>416</Customer_ID>
		<Customer_Name>Aurelia Bush</Customer_Name>
		<Customer_Email>ligula.nullam@yahoo.couk</Customer_Email>
		<Customer_Phone>(710) 766-1292</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-24</last_update>
	</record>
	<record>
		<Customer_PK>154</Customer_PK>
		<Customer_ID>353</Customer_ID>
		<Customer_Name>Melodie Jacobs</Customer_Name>
		<Customer_Email>id.sapien@outlook.org</Customer_Email>
		<Customer_Phone>(484) 622-5181</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-12</last_update>
	</record>
	<record>
		<Customer_PK>155</Customer_PK>
		<Customer_ID>194</Customer_ID>
		<Customer_Name>Raya Ayala</Customer_Name>
		<Customer_Email>nulla.ante@google.ca</Customer_Email>
		<Customer_Phone>(734) 845-9563</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-30</last_update>
	</record>
	<record>
		<Customer_PK>156</Customer_PK>
		<Customer_ID>187</Customer_ID>
		<Customer_Name>Carly Atkins</Customer_Name>
		<Customer_Email>porttitor.eros@google.couk</Customer_Email>
		<Customer_Phone>1-678-746-8211</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-1-18</last_update>
	</record>
	<record>
		<Customer_PK>157</Customer_PK>
		<Customer_ID>44</Customer_ID>
		<Customer_Name>Kamal Erickson</Customer_Name>
		<Customer_Email>fusce.fermentum@outlook.com</Customer_Email>
		<Customer_Phone>1-222-631-0418</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-8</last_update>
	</record>
	<record>
		<Customer_PK>158</Customer_PK>
		<Customer_ID>43</Customer_ID>
		<Customer_Name>Mollie Lynn</Customer_Name>
		<Customer_Email>a.magna@hotmail.org</Customer_Email>
		<Customer_Phone>1-726-424-3665</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-21</last_update>
	</record>
	<record>
		<Customer_PK>159</Customer_PK>
		<Customer_ID>54</Customer_ID>
		<Customer_Name>Hanae Berger</Customer_Name>
		<Customer_Email>vel.convallis@aol.ca</Customer_Email>
		<Customer_Phone>(837) 474-3530</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-4-5</last_update>
	</record>
	<record>
		<Customer_PK>160</Customer_PK>
		<Customer_ID>102</Customer_ID>
		<Customer_Name>Veda Keller</Customer_Name>
		<Customer_Email>in@hotmail.edu</Customer_Email>
		<Customer_Phone>1-975-337-6267</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-10</last_update>
	</record>
	<record>
		<Customer_PK>161</Customer_PK>
		<Customer_ID>130</Customer_ID>
		<Customer_Name>Garrett Guthrie</Customer_Name>
		<Customer_Email>vel@outlook.edu</Customer_Email>
		<Customer_Phone>(632) 736-2585</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-15</last_update>
	</record>
	<record>
		<Customer_PK>162</Customer_PK>
		<Customer_ID>284</Customer_ID>
		<Customer_Name>Rhonda Knox</Customer_Name>
		<Customer_Email>nunc.risus@protonmail.ca</Customer_Email>
		<Customer_Phone>(460) 457-7786</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-13</last_update>
	</record>
	<record>
		<Customer_PK>163</Customer_PK>
		<Customer_ID>435</Customer_ID>
		<Customer_Name>Jaden Woodward</Customer_Name>
		<Customer_Email>ultrices@yahoo.com</Customer_Email>
		<Customer_Phone>(427) 723-5588</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-8-15</last_update>
	</record>
	<record>
		<Customer_PK>164</Customer_PK>
		<Customer_ID>173</Customer_ID>
		<Customer_Name>Zia Kerr</Customer_Name>
		<Customer_Email>a.felis.ullamcorper@outlook.couk</Customer_Email>
		<Customer_Phone>(245) 239-8562</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-9-2</last_update>
	</record>
	<record>
		<Customer_PK>165</Customer_PK>
		<Customer_ID>342</Customer_ID>
		<Customer_Name>Wyatt Tanner</Customer_Name>
		<Customer_Email>congue@protonmail.ca</Customer_Email>
		<Customer_Phone>(241) 271-7563</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-14</last_update>
	</record>
	<record>
		<Customer_PK>166</Customer_PK>
		<Customer_ID>369</Customer_ID>
		<Customer_Name>Diana Lynch</Customer_Name>
		<Customer_Email>eget.ipsum@google.edu</Customer_Email>
		<Customer_Phone>(592) 781-6674</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-8-17</last_update>
	</record>
	<record>
		<Customer_PK>167</Customer_PK>
		<Customer_ID>431</Customer_ID>
		<Customer_Name>September Cook</Customer_Name>
		<Customer_Email>lorem@google.org</Customer_Email>
		<Customer_Phone>(844) 227-2861</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-10</last_update>
	</record>
	<record>
		<Customer_PK>168</Customer_PK>
		<Customer_ID>202</Customer_ID>
		<Customer_Name>Maggy Kelley</Customer_Name>
		<Customer_Email>ut@icloud.net</Customer_Email>
		<Customer_Phone>1-681-478-2647</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-4-2</last_update>
	</record>
	<record>
		<Customer_PK>169</Customer_PK>
		<Customer_ID>205</Customer_ID>
		<Customer_Name>Sacha Donovan</Customer_Name>
		<Customer_Email>auctor.odio@icloud.couk</Customer_Email>
		<Customer_Phone>(383) 546-3875</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-18</last_update>
	</record>
	<record>
		<Customer_PK>170</Customer_PK>
		<Customer_ID>336</Customer_ID>
		<Customer_Name>Ishmael Fuentes</Customer_Name>
		<Customer_Email>aliquet@outlook.com</Customer_Email>
		<Customer_Phone>(245) 416-3393</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-1</last_update>
	</record>
	<record>
		<Customer_PK>171</Customer_PK>
		<Customer_ID>351</Customer_ID>
		<Customer_Name>Kiona Holden</Customer_Name>
		<Customer_Email>cubilia.curae@icloud.ca</Customer_Email>
		<Customer_Phone>1-657-833-6416</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-5-12</last_update>
	</record>
	<record>
		<Customer_PK>172</Customer_PK>
		<Customer_ID>59</Customer_ID>
		<Customer_Name>Prescott Lara</Customer_Name>
		<Customer_Email>consequat.dolor@outlook.edu</Customer_Email>
		<Customer_Phone>1-365-920-4125</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-27</last_update>
	</record>
	<record>
		<Customer_PK>173</Customer_PK>
		<Customer_ID>383</Customer_ID>
		<Customer_Name>Jamal Dillon</Customer_Name>
		<Customer_Email>mauris.blandit@aol.org</Customer_Email>
		<Customer_Phone>1-737-376-2384</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-6</last_update>
	</record>
	<record>
		<Customer_PK>174</Customer_PK>
		<Customer_ID>217</Customer_ID>
		<Customer_Name>Alyssa Bowers</Customer_Name>
		<Customer_Email>augue@yahoo.ca</Customer_Email>
		<Customer_Phone>1-656-561-3261</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-4-1</last_update>
	</record>
	<record>
		<Customer_PK>175</Customer_PK>
		<Customer_ID>437</Customer_ID>
		<Customer_Name>April Mason</Customer_Name>
		<Customer_Email>molestie.arcu@icloud.edu</Customer_Email>
		<Customer_Phone>(719) 861-1418</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-2-22</last_update>
	</record>
	<record>
		<Customer_PK>176</Customer_PK>
		<Customer_ID>283</Customer_ID>
		<Customer_Name>Tanisha Holcomb</Customer_Name>
		<Customer_Email>quis.accumsan.convallis@protonmail.couk</Customer_Email>
		<Customer_Phone>(305) 847-2233</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-1</last_update>
	</record>
	<record>
		<Customer_PK>177</Customer_PK>
		<Customer_ID>34</Customer_ID>
		<Customer_Name>Vera Gamble</Customer_Name>
		<Customer_Email>pede@google.net</Customer_Email>
		<Customer_Phone>(429) 285-5980</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-9</last_update>
	</record>
	<record>
		<Customer_PK>178</Customer_PK>
		<Customer_ID>112</Customer_ID>
		<Customer_Name>Hunter Reed</Customer_Name>
		<Customer_Email>sodales.nisi@icloud.com</Customer_Email>
		<Customer_Phone>1-699-431-6227</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-8-13</last_update>
	</record>
	<record>
		<Customer_PK>179</Customer_PK>
		<Customer_ID>460</Customer_ID>
		<Customer_Name>Ashton Whitney</Customer_Name>
		<Customer_Email>phasellus.fermentum.convallis@yahoo.org</Customer_Email>
		<Customer_Phone>1-321-897-8427</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-17</last_update>
	</record>
	<record>
		<Customer_PK>180</Customer_PK>
		<Customer_ID>121</Customer_ID>
		<Customer_Name>Jakeem Gentry</Customer_Name>
		<Customer_Email>suscipit@outlook.edu</Customer_Email>
		<Customer_Phone>1-758-691-1412</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-4-13</last_update>
	</record>
	<record>
		<Customer_PK>181</Customer_PK>
		<Customer_ID>332</Customer_ID>
		<Customer_Name>Marsden Bishop</Customer_Name>
		<Customer_Email>at.lacus.quisque@outlook.ca</Customer_Email>
		<Customer_Phone>(425) 553-8135</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-11-7</last_update>
	</record>
	<record>
		<Customer_PK>182</Customer_PK>
		<Customer_ID>5</Customer_ID>
		<Customer_Name>Austin Hammond</Customer_Name>
		<Customer_Email>diam.eu@yahoo.couk</Customer_Email>
		<Customer_Phone>(508) 642-7294</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-13</last_update>
	</record>
	<record>
		<Customer_PK>183</Customer_PK>
		<Customer_ID>37</Customer_ID>
		<Customer_Name>Griffin Mckee</Customer_Name>
		<Customer_Email>ut.lacus.nulla@hotmail.couk</Customer_Email>
		<Customer_Phone>(170) 804-0385</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-12</last_update>
	</record>
	<record>
		<Customer_PK>184</Customer_PK>
		<Customer_ID>349</Customer_ID>
		<Customer_Name>Carly Gray</Customer_Name>
		<Customer_Email>vitae@yahoo.com</Customer_Email>
		<Customer_Phone>1-145-482-6526</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-12</last_update>
	</record>
	<record>
		<Customer_PK>185</Customer_PK>
		<Customer_ID>308</Customer_ID>
		<Customer_Name>Rinah Leon</Customer_Name>
		<Customer_Email>nulla.ante@protonmail.ca</Customer_Email>
		<Customer_Phone>(940) 469-8647</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-11-6</last_update>
	</record>
	<record>
		<Customer_PK>186</Customer_PK>
		<Customer_ID>454</Customer_ID>
		<Customer_Name>Jerome Zimmerman</Customer_Name>
		<Customer_Email>egestas@google.com</Customer_Email>
		<Customer_Phone>(491) 370-2274</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-20</last_update>
	</record>
	<record>
		<Customer_PK>187</Customer_PK>
		<Customer_ID>468</Customer_ID>
		<Customer_Name>Eve Todd</Customer_Name>
		<Customer_Email>mi.felis@hotmail.couk</Customer_Email>
		<Customer_Phone>(447) 354-6373</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-24</last_update>
	</record>
	<record>
		<Customer_PK>188</Customer_PK>
		<Customer_ID>125</Customer_ID>
		<Customer_Name>Catherine Kane</Customer_Name>
		<Customer_Email>auctor.velit@protonmail.org</Customer_Email>
		<Customer_Phone>(876) 297-7829</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-19</last_update>
	</record>
	<record>
		<Customer_PK>189</Customer_PK>
		<Customer_ID>116</Customer_ID>
		<Customer_Name>Julie Velasquez</Customer_Name>
		<Customer_Email>sed.orci.lobortis@google.edu</Customer_Email>
		<Customer_Phone>1-409-419-5394</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-8</last_update>
	</record>
	<record>
		<Customer_PK>190</Customer_PK>
		<Customer_ID>176</Customer_ID>
		<Customer_Name>Vernon Shelton</Customer_Name>
		<Customer_Email>vulputate.lacus.cras@protonmail.couk</Customer_Email>
		<Customer_Phone>(389) 809-4287</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-16</last_update>
	</record>
	<record>
		<Customer_PK>191</Customer_PK>
		<Customer_ID>237</Customer_ID>
		<Customer_Name>Violet Ramos</Customer_Name>
		<Customer_Email>eu@icloud.net</Customer_Email>
		<Customer_Phone>(131) 794-1841</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-4-12</last_update>
	</record>
	<record>
		<Customer_PK>192</Customer_PK>
		<Customer_ID>72</Customer_ID>
		<Customer_Name>Dean Beach</Customer_Name>
		<Customer_Email>et@google.ca</Customer_Email>
		<Customer_Phone>1-522-117-8443</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-11-5</last_update>
	</record>
	<record>
		<Customer_PK>193</Customer_PK>
		<Customer_ID>459</Customer_ID>
		<Customer_Name>Ignatius Cannon</Customer_Name>
		<Customer_Email>enim@yahoo.com</Customer_Email>
		<Customer_Phone>1-721-562-1249</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-15</last_update>
	</record>
	<record>
		<Customer_PK>194</Customer_PK>
		<Customer_ID>339</Customer_ID>
		<Customer_Name>Vivien Wade</Customer_Name>
		<Customer_Email>penatibus.et.magnis@protonmail.edu</Customer_Email>
		<Customer_Phone>1-930-427-7117</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-7</last_update>
	</record>
	<record>
		<Customer_PK>195</Customer_PK>
		<Customer_ID>290</Customer_ID>
		<Customer_Name>Geoffrey Dean</Customer_Name>
		<Customer_Email>pulvinar.arcu@hotmail.org</Customer_Email>
		<Customer_Phone>1-722-848-3484</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-17</last_update>
	</record>
	<record>
		<Customer_PK>196</Customer_PK>
		<Customer_ID>311</Customer_ID>
		<Customer_Name>Gil Blair</Customer_Name>
		<Customer_Email>eget.varius@outlook.edu</Customer_Email>
		<Customer_Phone>(459) 363-8274</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-18</last_update>
	</record>
	<record>
		<Customer_PK>197</Customer_PK>
		<Customer_ID>451</Customer_ID>
		<Customer_Name>Matthew Carlson</Customer_Name>
		<Customer_Email>tincidunt.donec@icloud.net</Customer_Email>
		<Customer_Phone>(222) 367-1333</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-24</last_update>
	</record>
	<record>
		<Customer_PK>198</Customer_PK>
		<Customer_ID>11</Customer_ID>
		<Customer_Name>Willa Robles</Customer_Name>
		<Customer_Email>felis@google.ca</Customer_Email>
		<Customer_Phone>1-644-126-2024</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-19</last_update>
	</record>
	<record>
		<Customer_PK>199</Customer_PK>
		<Customer_ID>476</Customer_ID>
		<Customer_Name>Miriam Welch</Customer_Name>
		<Customer_Email>mauris.vel@icloud.ca</Customer_Email>
		<Customer_Phone>1-300-606-8162</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-10-17</last_update>
	</record>
	<record>
		<Customer_PK>200</Customer_PK>
		<Customer_ID>81</Customer_ID>
		<Customer_Name>Holly Fowler</Customer_Name>
		<Customer_Email>volutpat.ornare@icloud.edu</Customer_Email>
		<Customer_Phone>1-722-550-5738</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-23</last_update>
	</record>
	<record>
		<Customer_PK>201</Customer_PK>
		<Customer_ID>189</Customer_ID>
		<Customer_Name>Veda Lane</Customer_Name>
		<Customer_Email>orci.luctus@hotmail.org</Customer_Email>
		<Customer_Phone>1-757-865-4867</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-19</last_update>
	</record>
	<record>
		<Customer_PK>202</Customer_PK>
		<Customer_ID>309</Customer_ID>
		<Customer_Name>Alvin Nunez</Customer_Name>
		<Customer_Email>aptent.taciti@yahoo.edu</Customer_Email>
		<Customer_Phone>(578) 772-2412</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-18</last_update>
	</record>
	<record>
		<Customer_PK>203</Customer_PK>
		<Customer_ID>357</Customer_ID>
		<Customer_Name>Eagan Larson</Customer_Name>
		<Customer_Email>parturient.montes@hotmail.org</Customer_Email>
		<Customer_Phone>(278) 787-9644</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-3</last_update>
	</record>
	<record>
		<Customer_PK>204</Customer_PK>
		<Customer_ID>265</Customer_ID>
		<Customer_Name>Clarke Love</Customer_Name>
		<Customer_Email>id.ante@icloud.net</Customer_Email>
		<Customer_Phone>1-646-715-1260</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-11-10</last_update>
	</record>
	<record>
		<Customer_PK>205</Customer_PK>
		<Customer_ID>145</Customer_ID>
		<Customer_Name>Cathleen Dean</Customer_Name>
		<Customer_Email>urna.nec@yahoo.ca</Customer_Email>
		<Customer_Phone>1-685-543-5637</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-11-12</last_update>
	</record>
	<record>
		<Customer_PK>206</Customer_PK>
		<Customer_ID>449</Customer_ID>
		<Customer_Name>Jack Jones</Customer_Name>
		<Customer_Email>tellus@hotmail.couk</Customer_Email>
		<Customer_Phone>1-532-462-9608</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-4</last_update>
	</record>
	<record>
		<Customer_PK>207</Customer_PK>
		<Customer_ID>358</Customer_ID>
		<Customer_Name>Isadora Rodgers</Customer_Name>
		<Customer_Email>convallis.dolor@google.couk</Customer_Email>
		<Customer_Phone>1-508-611-4663</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-25</last_update>
	</record>
	<record>
		<Customer_PK>208</Customer_PK>
		<Customer_ID>415</Customer_ID>
		<Customer_Name>Norman Terry</Customer_Name>
		<Customer_Email>neque.morbi@google.ca</Customer_Email>
		<Customer_Phone>(749) 258-4282</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-22</last_update>
	</record>
	<record>
		<Customer_PK>209</Customer_PK>
		<Customer_ID>20</Customer_ID>
		<Customer_Name>Wesley Anthony</Customer_Name>
		<Customer_Email>suspendisse.dui@outlook.edu</Customer_Email>
		<Customer_Phone>1-391-576-3444</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-9-15</last_update>
	</record>
	<record>
		<Customer_PK>210</Customer_PK>
		<Customer_ID>101</Customer_ID>
		<Customer_Name>Kameko Dennis</Customer_Name>
		<Customer_Email>donec.est@protonmail.com</Customer_Email>
		<Customer_Phone>1-673-156-4447</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-9-16</last_update>
	</record>
	<record>
		<Customer_PK>211</Customer_PK>
		<Customer_ID>305</Customer_ID>
		<Customer_Name>Gray Lowe</Customer_Name>
		<Customer_Email>proin.non@outlook.ca</Customer_Email>
		<Customer_Phone>1-748-523-7296</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-23</last_update>
	</record>
	<record>
		<Customer_PK>212</Customer_PK>
		<Customer_ID>141</Customer_ID>
		<Customer_Name>Kennan Meadows</Customer_Name>
		<Customer_Email>aliquet.molestie@hotmail.edu</Customer_Email>
		<Customer_Phone>1-848-497-2545</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-21</last_update>
	</record>
	<record>
		<Customer_PK>213</Customer_PK>
		<Customer_ID>109</Customer_ID>
		<Customer_Name>Kameko Humphrey</Customer_Name>
		<Customer_Email>curabitur.consequat@hotmail.ca</Customer_Email>
		<Customer_Phone>(881) 581-3621</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-9-12</last_update>
	</record>
	<record>
		<Customer_PK>214</Customer_PK>
		<Customer_ID>134</Customer_ID>
		<Customer_Name>Whilemina Baker</Customer_Name>
		<Customer_Email>eget.ipsum@hotmail.edu</Customer_Email>
		<Customer_Phone>(630) 664-7544</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-12</last_update>
	</record>
	<record>
		<Customer_PK>215</Customer_PK>
		<Customer_ID>230</Customer_ID>
		<Customer_Name>Constance Eaton</Customer_Name>
		<Customer_Email>magna.suspendisse@aol.edu</Customer_Email>
		<Customer_Phone>(101) 115-1473</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-20</last_update>
	</record>
	<record>
		<Customer_PK>216</Customer_PK>
		<Customer_ID>130</Customer_ID>
		<Customer_Name>Odessa Glenn</Customer_Name>
		<Customer_Email>egestas.ligula@aol.com</Customer_Email>
		<Customer_Phone>1-516-485-3556</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-23</last_update>
	</record>
	<record>
		<Customer_PK>217</Customer_PK>
		<Customer_ID>25</Customer_ID>
		<Customer_Name>Cameron Macias</Customer_Name>
		<Customer_Email>massa.mauris.vestibulum@yahoo.ca</Customer_Email>
		<Customer_Phone>(794) 307-5662</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-21</last_update>
	</record>
	<record>
		<Customer_PK>218</Customer_PK>
		<Customer_ID>247</Customer_ID>
		<Customer_Name>Lesley Mcfadden</Customer_Name>
		<Customer_Email>tellus.eu@protonmail.edu</Customer_Email>
		<Customer_Phone>(434) 642-2527</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-3</last_update>
	</record>
	<record>
		<Customer_PK>219</Customer_PK>
		<Customer_ID>343</Customer_ID>
		<Customer_Name>Jena Doyle</Customer_Name>
		<Customer_Email>elit.dictum@google.couk</Customer_Email>
		<Customer_Phone>1-116-418-2285</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-5</last_update>
	</record>
	<record>
		<Customer_PK>220</Customer_PK>
		<Customer_ID>106</Customer_ID>
		<Customer_Name>Damian Peters</Customer_Name>
		<Customer_Email>lectus.justo@google.org</Customer_Email>
		<Customer_Phone>1-477-404-8001</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-11-18</last_update>
	</record>
	<record>
		<Customer_PK>221</Customer_PK>
		<Customer_ID>245</Customer_ID>
		<Customer_Name>Marsden Hammond</Customer_Name>
		<Customer_Email>sociis.natoque@aol.org</Customer_Email>
		<Customer_Phone>1-577-275-4795</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-29</last_update>
	</record>
	<record>
		<Customer_PK>222</Customer_PK>
		<Customer_ID>146</Customer_ID>
		<Customer_Name>Nadine Cooper</Customer_Name>
		<Customer_Email>nulla.donec.non@hotmail.net</Customer_Email>
		<Customer_Phone>1-384-863-5103</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-5-1</last_update>
	</record>
	<record>
		<Customer_PK>223</Customer_PK>
		<Customer_ID>114</Customer_ID>
		<Customer_Name>Emery Gonzalez</Customer_Name>
		<Customer_Email>faucibus.leo@yahoo.com</Customer_Email>
		<Customer_Phone>(262) 712-9153</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-31</last_update>
	</record>
	<record>
		<Customer_PK>224</Customer_PK>
		<Customer_ID>213</Customer_ID>
		<Customer_Name>Joshua Caldwell</Customer_Name>
		<Customer_Email>vel.arcu@yahoo.edu</Customer_Email>
		<Customer_Phone>1-644-528-2714</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-22</last_update>
	</record>
	<record>
		<Customer_PK>225</Customer_PK>
		<Customer_ID>471</Customer_ID>
		<Customer_Name>Cleo Allen</Customer_Name>
		<Customer_Email>cras.dolor@protonmail.org</Customer_Email>
		<Customer_Phone>1-235-805-5161</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-23</last_update>
	</record>
	<record>
		<Customer_PK>226</Customer_PK>
		<Customer_ID>114</Customer_ID>
		<Customer_Name>Phelan Forbes</Customer_Name>
		<Customer_Email>etiam@protonmail.com</Customer_Email>
		<Customer_Phone>1-419-866-8125</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-10</last_update>
	</record>
	<record>
		<Customer_PK>227</Customer_PK>
		<Customer_ID>81</Customer_ID>
		<Customer_Name>Hoyt Glover</Customer_Name>
		<Customer_Email>nisl@aol.couk</Customer_Email>
		<Customer_Phone>(757) 280-1658</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-7</last_update>
	</record>
	<record>
		<Customer_PK>228</Customer_PK>
		<Customer_ID>338</Customer_ID>
		<Customer_Name>Jessamine Hoffman</Customer_Name>
		<Customer_Email>montes.nascetur@aol.org</Customer_Email>
		<Customer_Phone>1-380-197-7103</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-31</last_update>
	</record>
	<record>
		<Customer_PK>229</Customer_PK>
		<Customer_ID>15</Customer_ID>
		<Customer_Name>Aaron Wright</Customer_Name>
		<Customer_Email>dolor.vitae.dolor@outlook.couk</Customer_Email>
		<Customer_Phone>(381) 575-6376</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-8-15</last_update>
	</record>
	<record>
		<Customer_PK>230</Customer_PK>
		<Customer_ID>313</Customer_ID>
		<Customer_Name>Jael Dale</Customer_Name>
		<Customer_Email>dolor@yahoo.edu</Customer_Email>
		<Customer_Phone>1-318-648-8951</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-9</last_update>
	</record>
	<record>
		<Customer_PK>231</Customer_PK>
		<Customer_ID>424</Customer_ID>
		<Customer_Name>Thane Blankenship</Customer_Name>
		<Customer_Email>est.vitae@google.org</Customer_Email>
		<Customer_Phone>(692) 132-2585</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-20</last_update>
	</record>
	<record>
		<Customer_PK>232</Customer_PK>
		<Customer_ID>494</Customer_ID>
		<Customer_Name>Germane Lester</Customer_Name>
		<Customer_Email>nec.tempus@outlook.net</Customer_Email>
		<Customer_Phone>(753) 753-5075</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-7</last_update>
	</record>
	<record>
		<Customer_PK>233</Customer_PK>
		<Customer_ID>176</Customer_ID>
		<Customer_Name>Harriet Perez</Customer_Name>
		<Customer_Email>augue.sed@google.edu</Customer_Email>
		<Customer_Phone>(598) 901-4295</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-14</last_update>
	</record>
	<record>
		<Customer_PK>234</Customer_PK>
		<Customer_ID>75</Customer_ID>
		<Customer_Name>Hanna Larsen</Customer_Name>
		<Customer_Email>lectus.sit.amet@aol.edu</Customer_Email>
		<Customer_Phone>(752) 693-4943</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-7</last_update>
	</record>
	<record>
		<Customer_PK>235</Customer_PK>
		<Customer_ID>151</Customer_ID>
		<Customer_Name>Maile Vaughan</Customer_Name>
		<Customer_Email>nulla@google.edu</Customer_Email>
		<Customer_Phone>1-556-895-4412</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-5</last_update>
	</record>
	<record>
		<Customer_PK>236</Customer_PK>
		<Customer_ID>222</Customer_ID>
		<Customer_Name>Erica Mckee</Customer_Name>
		<Customer_Email>curabitur@google.ca</Customer_Email>
		<Customer_Phone>(716) 514-2631</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-30</last_update>
	</record>
	<record>
		<Customer_PK>237</Customer_PK>
		<Customer_ID>373</Customer_ID>
		<Customer_Name>Tatyana Henry</Customer_Name>
		<Customer_Email>phasellus.nulla@aol.couk</Customer_Email>
		<Customer_Phone>1-831-323-0498</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-28</last_update>
	</record>
	<record>
		<Customer_PK>238</Customer_PK>
		<Customer_ID>438</Customer_ID>
		<Customer_Name>Dahlia Nelson</Customer_Name>
		<Customer_Email>est@aol.ca</Customer_Email>
		<Customer_Phone>(945) 268-7639</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-4-20</last_update>
	</record>
	<record>
		<Customer_PK>239</Customer_PK>
		<Customer_ID>259</Customer_ID>
		<Customer_Name>Gannon Reilly</Customer_Name>
		<Customer_Email>donec.sollicitudin@google.org</Customer_Email>
		<Customer_Phone>(851) 245-8579</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-8</last_update>
	</record>
	<record>
		<Customer_PK>240</Customer_PK>
		<Customer_ID>239</Customer_ID>
		<Customer_Name>Dorian Hood</Customer_Name>
		<Customer_Email>tortor.nunc.commodo@outlook.org</Customer_Email>
		<Customer_Phone>1-635-484-8225</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-14</last_update>
	</record>
	<record>
		<Customer_PK>241</Customer_PK>
		<Customer_ID>174</Customer_ID>
		<Customer_Name>Jeanette Conner</Customer_Name>
		<Customer_Email>eleifend.non@outlook.couk</Customer_Email>
		<Customer_Phone>(285) 478-2245</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-14</last_update>
	</record>
	<record>
		<Customer_PK>242</Customer_PK>
		<Customer_ID>127</Customer_ID>
		<Customer_Name>Ulla Thomas</Customer_Name>
		<Customer_Email>risus.quis.diam@google.ca</Customer_Email>
		<Customer_Phone>(402) 701-2614</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-24</last_update>
	</record>
	<record>
		<Customer_PK>243</Customer_PK>
		<Customer_ID>338</Customer_ID>
		<Customer_Name>Guy Mckenzie</Customer_Name>
		<Customer_Email>orci@protonmail.edu</Customer_Email>
		<Customer_Phone>(688) 885-1528</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-21</last_update>
	</record>
	<record>
		<Customer_PK>244</Customer_PK>
		<Customer_ID>268</Customer_ID>
		<Customer_Name>Gillian Hooper</Customer_Name>
		<Customer_Email>mauris@hotmail.ca</Customer_Email>
		<Customer_Phone>1-812-893-8866</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-17</last_update>
	</record>
	<record>
		<Customer_PK>245</Customer_PK>
		<Customer_ID>106</Customer_ID>
		<Customer_Name>Hermione Barron</Customer_Name>
		<Customer_Email>risus.donec.egestas@protonmail.edu</Customer_Email>
		<Customer_Phone>(144) 932-5632</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-14</last_update>
	</record>
	<record>
		<Customer_PK>246</Customer_PK>
		<Customer_ID>51</Customer_ID>
		<Customer_Name>Marah Duke</Customer_Name>
		<Customer_Email>pharetra@hotmail.org</Customer_Email>
		<Customer_Phone>(962) 708-7714</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-6</last_update>
	</record>
	<record>
		<Customer_PK>247</Customer_PK>
		<Customer_ID>492</Customer_ID>
		<Customer_Name>Zachery Yang</Customer_Name>
		<Customer_Email>curabitur.dictum@icloud.org</Customer_Email>
		<Customer_Phone>1-947-231-0340</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-28</last_update>
	</record>
	<record>
		<Customer_PK>248</Customer_PK>
		<Customer_ID>230</Customer_ID>
		<Customer_Name>Myles Randall</Customer_Name>
		<Customer_Email>ullamcorper.viverra@protonmail.ca</Customer_Email>
		<Customer_Phone>1-534-355-6199</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-27</last_update>
	</record>
	<record>
		<Customer_PK>249</Customer_PK>
		<Customer_ID>254</Customer_ID>
		<Customer_Name>Nash Pratt</Customer_Name>
		<Customer_Email>vitae.erat.vel@google.couk</Customer_Email>
		<Customer_Phone>(260) 153-1918</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-4-22</last_update>
	</record>
	<record>
		<Customer_PK>250</Customer_PK>
		<Customer_ID>209</Customer_ID>
		<Customer_Name>Vanna Lawrence</Customer_Name>
		<Customer_Email>urna.et@outlook.com</Customer_Email>
		<Customer_Phone>1-875-717-2382</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-11-15</last_update>
	</record>
	<record>
		<Customer_PK>251</Customer_PK>
		<Customer_ID>155</Customer_ID>
		<Customer_Name>Nomlanga Petersen</Customer_Name>
		<Customer_Email>lectus.convallis@google.couk</Customer_Email>
		<Customer_Phone>1-564-332-8773</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-1</last_update>
	</record>
	<record>
		<Customer_PK>252</Customer_PK>
		<Customer_ID>95</Customer_ID>
		<Customer_Name>Bryar Skinner</Customer_Name>
		<Customer_Email>et@hotmail.couk</Customer_Email>
		<Customer_Phone>(511) 431-8365</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-2</last_update>
	</record>
	<record>
		<Customer_PK>253</Customer_PK>
		<Customer_ID>107</Customer_ID>
		<Customer_Name>Kenneth Carson</Customer_Name>
		<Customer_Email>integer.urna@google.org</Customer_Email>
		<Customer_Phone>(448) 736-8247</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-9-13</last_update>
	</record>
	<record>
		<Customer_PK>254</Customer_PK>
		<Customer_ID>229</Customer_ID>
		<Customer_Name>Kirk Solomon</Customer_Name>
		<Customer_Email>nostra.per@hotmail.com</Customer_Email>
		<Customer_Phone>1-375-776-5088</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-10-21</last_update>
	</record>
	<record>
		<Customer_PK>255</Customer_PK>
		<Customer_ID>411</Customer_ID>
		<Customer_Name>Bert Lawson</Customer_Name>
		<Customer_Email>metus.urna@outlook.couk</Customer_Email>
		<Customer_Phone>(955) 367-1455</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-29</last_update>
	</record>
	<record>
		<Customer_PK>256</Customer_PK>
		<Customer_ID>186</Customer_ID>
		<Customer_Name>Mechelle Lane</Customer_Name>
		<Customer_Email>nam@outlook.org</Customer_Email>
		<Customer_Phone>1-747-687-4130</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-9</last_update>
	</record>
	<record>
		<Customer_PK>257</Customer_PK>
		<Customer_ID>230</Customer_ID>
		<Customer_Name>Hanna Silva</Customer_Name>
		<Customer_Email>nostra.per.inceptos@yahoo.edu</Customer_Email>
		<Customer_Phone>1-538-553-2773</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-17</last_update>
	</record>
	<record>
		<Customer_PK>258</Customer_PK>
		<Customer_ID>189</Customer_ID>
		<Customer_Name>Ali Hamilton</Customer_Name>
		<Customer_Email>dolor.tempus@google.ca</Customer_Email>
		<Customer_Phone>(602) 665-5685</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-29</last_update>
	</record>
	<record>
		<Customer_PK>259</Customer_PK>
		<Customer_ID>285</Customer_ID>
		<Customer_Name>Shay Atkins</Customer_Name>
		<Customer_Email>tincidunt.vehicula@google.com</Customer_Email>
		<Customer_Phone>1-249-723-0407</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-11</last_update>
	</record>
	<record>
		<Customer_PK>260</Customer_PK>
		<Customer_ID>107</Customer_ID>
		<Customer_Name>Craig Wilcox</Customer_Name>
		<Customer_Email>dui.in@google.org</Customer_Email>
		<Customer_Phone>1-936-411-1188</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-13</last_update>
	</record>
	<record>
		<Customer_PK>261</Customer_PK>
		<Customer_ID>96</Customer_ID>
		<Customer_Name>Dorothy Solomon</Customer_Name>
		<Customer_Email>lobortis@hotmail.net</Customer_Email>
		<Customer_Phone>(138) 668-1464</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-1</last_update>
	</record>
	<record>
		<Customer_PK>262</Customer_PK>
		<Customer_ID>376</Customer_ID>
		<Customer_Name>Alec Chapman</Customer_Name>
		<Customer_Email>duis.dignissim.tempor@hotmail.com</Customer_Email>
		<Customer_Phone>(378) 569-9256</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-20</last_update>
	</record>
	<record>
		<Customer_PK>263</Customer_PK>
		<Customer_ID>362</Customer_ID>
		<Customer_Name>Thor Hodges</Customer_Name>
		<Customer_Email>proin.velit.sed@hotmail.net</Customer_Email>
		<Customer_Phone>(611) 220-6437</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-2-26</last_update>
	</record>
	<record>
		<Customer_PK>264</Customer_PK>
		<Customer_ID>276</Customer_ID>
		<Customer_Name>Wade Cameron</Customer_Name>
		<Customer_Email>turpis.egestas@yahoo.net</Customer_Email>
		<Customer_Phone>1-513-515-2931</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-11</last_update>
	</record>
	<record>
		<Customer_PK>265</Customer_PK>
		<Customer_ID>302</Customer_ID>
		<Customer_Name>Kadeem Blanchard</Customer_Name>
		<Customer_Email>dolor.tempus.non@yahoo.couk</Customer_Email>
		<Customer_Phone>1-692-378-2773</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-5</last_update>
	</record>
	<record>
		<Customer_PK>266</Customer_PK>
		<Customer_ID>363</Customer_ID>
		<Customer_Name>Beatrice Hall</Customer_Name>
		<Customer_Email>consectetuer.adipiscing.elit@hotmail.couk</Customer_Email>
		<Customer_Phone>1-236-193-5427</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-4-5</last_update>
	</record>
	<record>
		<Customer_PK>267</Customer_PK>
		<Customer_ID>208</Customer_ID>
		<Customer_Name>Riley Blankenship</Customer_Name>
		<Customer_Email>velit.in.aliquet@aol.couk</Customer_Email>
		<Customer_Phone>1-292-266-6175</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-25</last_update>
	</record>
	<record>
		<Customer_PK>268</Customer_PK>
		<Customer_ID>129</Customer_ID>
		<Customer_Name>Ayanna Herrera</Customer_Name>
		<Customer_Email>eleifend.nunc.risus@protonmail.couk</Customer_Email>
		<Customer_Phone>(168) 823-6721</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-18</last_update>
	</record>
	<record>
		<Customer_PK>269</Customer_PK>
		<Customer_ID>231</Customer_ID>
		<Customer_Name>Cara Pena</Customer_Name>
		<Customer_Email>integer.id@hotmail.org</Customer_Email>
		<Customer_Phone>1-462-884-5916</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-22</last_update>
	</record>
	<record>
		<Customer_PK>270</Customer_PK>
		<Customer_ID>339</Customer_ID>
		<Customer_Name>Devin Washington</Customer_Name>
		<Customer_Email>quis@outlook.ca</Customer_Email>
		<Customer_Phone>(762) 435-8832</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-5-7</last_update>
	</record>
	<record>
		<Customer_PK>271</Customer_PK>
		<Customer_ID>410</Customer_ID>
		<Customer_Name>Dexter Terrell</Customer_Name>
		<Customer_Email>vel.mauris@protonmail.edu</Customer_Email>
		<Customer_Phone>(222) 267-3379</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-8</last_update>
	</record>
	<record>
		<Customer_PK>272</Customer_PK>
		<Customer_ID>19</Customer_ID>
		<Customer_Name>Neve Richard</Customer_Name>
		<Customer_Email>rutrum.urna@protonmail.couk</Customer_Email>
		<Customer_Phone>1-275-758-0215</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-2</last_update>
	</record>
	<record>
		<Customer_PK>273</Customer_PK>
		<Customer_ID>354</Customer_ID>
		<Customer_Name>Emery Hunter</Customer_Name>
		<Customer_Email>lectus@icloud.edu</Customer_Email>
		<Customer_Phone>(343) 126-0113</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-4-23</last_update>
	</record>
	<record>
		<Customer_PK>274</Customer_PK>
		<Customer_ID>6</Customer_ID>
		<Customer_Name>Nathaniel Hart</Customer_Name>
		<Customer_Email>non.leo@hotmail.couk</Customer_Email>
		<Customer_Phone>1-300-777-0242</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-8</last_update>
	</record>
	<record>
		<Customer_PK>275</Customer_PK>
		<Customer_ID>220</Customer_ID>
		<Customer_Name>Yvette Ellis</Customer_Name>
		<Customer_Email>morbi@icloud.couk</Customer_Email>
		<Customer_Phone>(787) 642-4787</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-21</last_update>
	</record>
	<record>
		<Customer_PK>276</Customer_PK>
		<Customer_ID>172</Customer_ID>
		<Customer_Name>Cailin Alvarado</Customer_Name>
		<Customer_Email>cubilia@icloud.couk</Customer_Email>
		<Customer_Phone>1-539-383-8158</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-17</last_update>
	</record>
	<record>
		<Customer_PK>277</Customer_PK>
		<Customer_ID>186</Customer_ID>
		<Customer_Name>Ebony Cruz</Customer_Name>
		<Customer_Email>lectus@outlook.edu</Customer_Email>
		<Customer_Phone>(422) 831-1832</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-5</last_update>
	</record>
	<record>
		<Customer_PK>278</Customer_PK>
		<Customer_ID>117</Customer_ID>
		<Customer_Name>Rigel Lambert</Customer_Name>
		<Customer_Email>dolor.fusce@hotmail.org</Customer_Email>
		<Customer_Phone>(558) 666-3640</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-27</last_update>
	</record>
	<record>
		<Customer_PK>279</Customer_PK>
		<Customer_ID>207</Customer_ID>
		<Customer_Name>Caleb Chaney</Customer_Name>
		<Customer_Email>mi.fringilla.mi@aol.couk</Customer_Email>
		<Customer_Phone>1-167-481-8592</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-10-3</last_update>
	</record>
	<record>
		<Customer_PK>280</Customer_PK>
		<Customer_ID>160</Customer_ID>
		<Customer_Name>Noelani Manning</Customer_Name>
		<Customer_Email>justo.praesent.luctus@yahoo.net</Customer_Email>
		<Customer_Phone>(543) 677-7225</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-23</last_update>
	</record>
	<record>
		<Customer_PK>281</Customer_PK>
		<Customer_ID>45</Customer_ID>
		<Customer_Name>Carson Leblanc</Customer_Name>
		<Customer_Email>pede@outlook.ca</Customer_Email>
		<Customer_Phone>(387) 321-3443</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-8-13</last_update>
	</record>
	<record>
		<Customer_PK>282</Customer_PK>
		<Customer_ID>276</Customer_ID>
		<Customer_Name>Brooke Hooper</Customer_Name>
		<Customer_Email>sagittis.placerat.cras@google.ca</Customer_Email>
		<Customer_Phone>(542) 581-1719</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-23</last_update>
	</record>
	<record>
		<Customer_PK>283</Customer_PK>
		<Customer_ID>264</Customer_ID>
		<Customer_Name>Rachel Holmes</Customer_Name>
		<Customer_Email>montes.nascetur.ridiculus@hotmail.org</Customer_Email>
		<Customer_Phone>(271) 514-6448</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-21</last_update>
	</record>
	<record>
		<Customer_PK>284</Customer_PK>
		<Customer_ID>306</Customer_ID>
		<Customer_Name>Colorado Ballard</Customer_Name>
		<Customer_Email>nibh@icloud.org</Customer_Email>
		<Customer_Phone>(425) 847-3323</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-26</last_update>
	</record>
	<record>
		<Customer_PK>285</Customer_PK>
		<Customer_ID>412</Customer_ID>
		<Customer_Name>Sonya Vega</Customer_Name>
		<Customer_Email>aliquam@icloud.com</Customer_Email>
		<Customer_Phone>(456) 436-9680</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-8</last_update>
	</record>
	<record>
		<Customer_PK>286</Customer_PK>
		<Customer_ID>376</Customer_ID>
		<Customer_Name>Kane Berger</Customer_Name>
		<Customer_Email>tincidunt@outlook.edu</Customer_Email>
		<Customer_Phone>(674) 523-3715</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-2</last_update>
	</record>
	<record>
		<Customer_PK>287</Customer_PK>
		<Customer_ID>81</Customer_ID>
		<Customer_Name>Alma Faulkner</Customer_Name>
		<Customer_Email>nunc.est@icloud.net</Customer_Email>
		<Customer_Phone>1-695-482-7223</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-9-24</last_update>
	</record>
	<record>
		<Customer_PK>288</Customer_PK>
		<Customer_ID>229</Customer_ID>
		<Customer_Name>Walter Whitfield</Customer_Name>
		<Customer_Email>ante.iaculis.nec@google.couk</Customer_Email>
		<Customer_Phone>(143) 617-3233</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-9</last_update>
	</record>
	<record>
		<Customer_PK>289</Customer_PK>
		<Customer_ID>112</Customer_ID>
		<Customer_Name>Yen Mckenzie</Customer_Name>
		<Customer_Email>porttitor.interdum.sed@google.couk</Customer_Email>
		<Customer_Phone>(433) 465-9626</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-8-18</last_update>
	</record>
	<record>
		<Customer_PK>290</Customer_PK>
		<Customer_ID>315</Customer_ID>
		<Customer_Name>Carter Griffin</Customer_Name>
		<Customer_Email>eu.euismod@hotmail.com</Customer_Email>
		<Customer_Phone>(956) 346-4834</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-19</last_update>
	</record>
	<record>
		<Customer_PK>291</Customer_PK>
		<Customer_ID>309</Customer_ID>
		<Customer_Name>Baxter Gregory</Customer_Name>
		<Customer_Email>libero.et@outlook.edu</Customer_Email>
		<Customer_Phone>1-164-811-6426</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-23</last_update>
	</record>
	<record>
		<Customer_PK>292</Customer_PK>
		<Customer_ID>481</Customer_ID>
		<Customer_Name>Reuben Valentine</Customer_Name>
		<Customer_Email>aliquam.ultrices@outlook.edu</Customer_Email>
		<Customer_Phone>1-731-459-5636</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-14</last_update>
	</record>
	<record>
		<Customer_PK>293</Customer_PK>
		<Customer_ID>496</Customer_ID>
		<Customer_Name>Ahmed Sexton</Customer_Name>
		<Customer_Email>eget@hotmail.com</Customer_Email>
		<Customer_Phone>1-842-259-7433</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-10</last_update>
	</record>
	<record>
		<Customer_PK>294</Customer_PK>
		<Customer_ID>258</Customer_ID>
		<Customer_Name>Lunea Lawson</Customer_Name>
		<Customer_Email>mollis.duis@protonmail.couk</Customer_Email>
		<Customer_Phone>1-474-957-2677</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-12</last_update>
	</record>
	<record>
		<Customer_PK>295</Customer_PK>
		<Customer_ID>121</Customer_ID>
		<Customer_Name>Bevis Frye</Customer_Name>
		<Customer_Email>phasellus@icloud.net</Customer_Email>
		<Customer_Phone>(891) 812-5251</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-4-4</last_update>
	</record>
	<record>
		<Customer_PK>296</Customer_PK>
		<Customer_ID>262</Customer_ID>
		<Customer_Name>Victoria Miles</Customer_Name>
		<Customer_Email>vel.sapien@outlook.edu</Customer_Email>
		<Customer_Phone>(687) 550-3433</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-30</last_update>
	</record>
	<record>
		<Customer_PK>297</Customer_PK>
		<Customer_ID>56</Customer_ID>
		<Customer_Name>Dorian Waller</Customer_Name>
		<Customer_Email>et.nunc@aol.com</Customer_Email>
		<Customer_Phone>(865) 342-0313</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-15</last_update>
	</record>
	<record>
		<Customer_PK>298</Customer_PK>
		<Customer_ID>101</Customer_ID>
		<Customer_Name>Alec Simmons</Customer_Name>
		<Customer_Email>id.libero.donec@outlook.couk</Customer_Email>
		<Customer_Phone>1-847-394-4519</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-3</last_update>
	</record>
	<record>
		<Customer_PK>299</Customer_PK>
		<Customer_ID>150</Customer_ID>
		<Customer_Name>Aurora Gutierrez</Customer_Name>
		<Customer_Email>eu.eleifend.nec@icloud.net</Customer_Email>
		<Customer_Phone>(658) 373-4312</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-8-7</last_update>
	</record>
	<record>
		<Customer_PK>300</Customer_PK>
		<Customer_ID>203</Customer_ID>
		<Customer_Name>Skyler Bright</Customer_Name>
		<Customer_Email>vulputate@aol.com</Customer_Email>
		<Customer_Phone>1-465-873-7649</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-6</last_update>
	</record>
	<record>
		<Customer_PK>301</Customer_PK>
		<Customer_ID>437</Customer_ID>
		<Customer_Name>Iona Luna</Customer_Name>
		<Customer_Email>non@aol.ca</Customer_Email>
		<Customer_Phone>1-434-336-1610</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-9</last_update>
	</record>
	<record>
		<Customer_PK>302</Customer_PK>
		<Customer_ID>381</Customer_ID>
		<Customer_Name>Patience Oliver</Customer_Name>
		<Customer_Email>nec.luctus.felis@google.org</Customer_Email>
		<Customer_Phone>1-585-339-4279</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-12</last_update>
	</record>
	<record>
		<Customer_PK>303</Customer_PK>
		<Customer_ID>405</Customer_ID>
		<Customer_Name>Astra Heath</Customer_Name>
		<Customer_Email>lectus.sit@yahoo.com</Customer_Email>
		<Customer_Phone>1-465-794-6713</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-15</last_update>
	</record>
	<record>
		<Customer_PK>304</Customer_PK>
		<Customer_ID>139</Customer_ID>
		<Customer_Name>Robert Patton</Customer_Name>
		<Customer_Email>facilisis.magna.tellus@protonmail.edu</Customer_Email>
		<Customer_Phone>1-271-427-9476</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-12</last_update>
	</record>
	<record>
		<Customer_PK>305</Customer_PK>
		<Customer_ID>136</Customer_ID>
		<Customer_Name>Slade Sandoval</Customer_Name>
		<Customer_Email>etiam.vestibulum@protonmail.net</Customer_Email>
		<Customer_Phone>1-463-784-0614</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-24</last_update>
	</record>
	<record>
		<Customer_PK>306</Customer_PK>
		<Customer_ID>313</Customer_ID>
		<Customer_Name>Lance Owen</Customer_Name>
		<Customer_Email>duis.at.lacus@protonmail.org</Customer_Email>
		<Customer_Phone>(332) 299-5440</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-8-25</last_update>
	</record>
	<record>
		<Customer_PK>307</Customer_PK>
		<Customer_ID>396</Customer_ID>
		<Customer_Name>Kibo Luna</Customer_Name>
		<Customer_Email>molestie.dapibus@hotmail.com</Customer_Email>
		<Customer_Phone>(117) 664-8845</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-8</last_update>
	</record>
	<record>
		<Customer_PK>308</Customer_PK>
		<Customer_ID>218</Customer_ID>
		<Customer_Name>Andrew York</Customer_Name>
		<Customer_Email>rutrum@protonmail.org</Customer_Email>
		<Customer_Phone>1-413-882-9356</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-14</last_update>
	</record>
	<record>
		<Customer_PK>309</Customer_PK>
		<Customer_ID>354</Customer_ID>
		<Customer_Name>Alden Boone</Customer_Name>
		<Customer_Email>volutpat.nulla@yahoo.couk</Customer_Email>
		<Customer_Phone>(825) 658-6278</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-17</last_update>
	</record>
	<record>
		<Customer_PK>310</Customer_PK>
		<Customer_ID>484</Customer_ID>
		<Customer_Name>Brian Espinoza</Customer_Name>
		<Customer_Email>proin.nisl@hotmail.edu</Customer_Email>
		<Customer_Phone>(724) 843-6313</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-4-11</last_update>
	</record>
	<record>
		<Customer_PK>311</Customer_PK>
		<Customer_ID>128</Customer_ID>
		<Customer_Name>Jade Cooper</Customer_Name>
		<Customer_Email>nunc@outlook.org</Customer_Email>
		<Customer_Phone>(654) 569-2478</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-4</last_update>
	</record>
	<record>
		<Customer_PK>312</Customer_PK>
		<Customer_ID>177</Customer_ID>
		<Customer_Name>Urielle Barrett</Customer_Name>
		<Customer_Email>duis.sit.amet@icloud.couk</Customer_Email>
		<Customer_Phone>(956) 790-8282</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-8-9</last_update>
	</record>
	<record>
		<Customer_PK>313</Customer_PK>
		<Customer_ID>17</Customer_ID>
		<Customer_Name>Astra Bennett</Customer_Name>
		<Customer_Email>hymenaeos.mauris@protonmail.ca</Customer_Email>
		<Customer_Phone>1-193-222-8622</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-1</last_update>
	</record>
	<record>
		<Customer_PK>314</Customer_PK>
		<Customer_ID>389</Customer_ID>
		<Customer_Name>Cruz Mayer</Customer_Name>
		<Customer_Email>est@yahoo.ca</Customer_Email>
		<Customer_Phone>1-666-665-9602</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-16</last_update>
	</record>
	<record>
		<Customer_PK>315</Customer_PK>
		<Customer_ID>230</Customer_ID>
		<Customer_Name>Samson Berry</Customer_Name>
		<Customer_Email>nisl.sem@protonmail.net</Customer_Email>
		<Customer_Phone>(243) 581-1124</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-5</last_update>
	</record>
	<record>
		<Customer_PK>316</Customer_PK>
		<Customer_ID>266</Customer_ID>
		<Customer_Name>Devin Daniel</Customer_Name>
		<Customer_Email>auctor.quis@icloud.couk</Customer_Email>
		<Customer_Phone>(284) 732-3317</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-12</last_update>
	</record>
	<record>
		<Customer_PK>317</Customer_PK>
		<Customer_ID>338</Customer_ID>
		<Customer_Name>Amy Pickett</Customer_Name>
		<Customer_Email>vel.mauris.integer@aol.couk</Customer_Email>
		<Customer_Phone>1-851-420-6012</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-4-5</last_update>
	</record>
	<record>
		<Customer_PK>318</Customer_PK>
		<Customer_ID>92</Customer_ID>
		<Customer_Name>Eaton Shannon</Customer_Name>
		<Customer_Email>malesuada.vel.venenatis@outlook.org</Customer_Email>
		<Customer_Phone>(567) 265-5464</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-2</last_update>
	</record>
	<record>
		<Customer_PK>319</Customer_PK>
		<Customer_ID>108</Customer_ID>
		<Customer_Name>Jescie Oliver</Customer_Name>
		<Customer_Email>augue.porttitor@protonmail.edu</Customer_Email>
		<Customer_Phone>(132) 374-6947</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-5-3</last_update>
	</record>
	<record>
		<Customer_PK>320</Customer_PK>
		<Customer_ID>128</Customer_ID>
		<Customer_Name>Dara Haley</Customer_Name>
		<Customer_Email>nibh.dolor@protonmail.net</Customer_Email>
		<Customer_Phone>1-460-546-2332</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-26</last_update>
	</record>
	<record>
		<Customer_PK>321</Customer_PK>
		<Customer_ID>278</Customer_ID>
		<Customer_Name>Sade Mccoy</Customer_Name>
		<Customer_Email>est.nunc@aol.net</Customer_Email>
		<Customer_Phone>1-640-634-0906</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-10</last_update>
	</record>
	<record>
		<Customer_PK>322</Customer_PK>
		<Customer_ID>451</Customer_ID>
		<Customer_Name>Georgia Mcfarland</Customer_Name>
		<Customer_Email>lorem@outlook.couk</Customer_Email>
		<Customer_Phone>1-751-136-7570</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-19</last_update>
	</record>
	<record>
		<Customer_PK>323</Customer_PK>
		<Customer_ID>83</Customer_ID>
		<Customer_Name>Carter Perry</Customer_Name>
		<Customer_Email>sit.amet.ornare@google.com</Customer_Email>
		<Customer_Phone>(649) 998-8824</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-8-16</last_update>
	</record>
	<record>
		<Customer_PK>324</Customer_PK>
		<Customer_ID>471</Customer_ID>
		<Customer_Name>Tobias Newton</Customer_Name>
		<Customer_Email>curae.donec.tincidunt@hotmail.couk</Customer_Email>
		<Customer_Phone>1-656-543-2332</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-22</last_update>
	</record>
	<record>
		<Customer_PK>325</Customer_PK>
		<Customer_ID>355</Customer_ID>
		<Customer_Name>Karina Pate</Customer_Name>
		<Customer_Email>massa@icloud.edu</Customer_Email>
		<Customer_Phone>1-594-320-6174</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-4-6</last_update>
	</record>
	<record>
		<Customer_PK>326</Customer_PK>
		<Customer_ID>366</Customer_ID>
		<Customer_Name>Valentine Cote</Customer_Name>
		<Customer_Email>luctus.curabitur@google.couk</Customer_Email>
		<Customer_Phone>(768) 848-0812</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-26</last_update>
	</record>
	<record>
		<Customer_PK>327</Customer_PK>
		<Customer_ID>234</Customer_ID>
		<Customer_Name>August Simpson</Customer_Name>
		<Customer_Email>ultricies.ligula@protonmail.ca</Customer_Email>
		<Customer_Phone>(338) 243-8238</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-12</last_update>
	</record>
	<record>
		<Customer_PK>328</Customer_PK>
		<Customer_ID>190</Customer_ID>
		<Customer_Name>Logan Garner</Customer_Name>
		<Customer_Email>eget.odio@google.ca</Customer_Email>
		<Customer_Phone>(425) 271-5902</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-8-27</last_update>
	</record>
	<record>
		<Customer_PK>329</Customer_PK>
		<Customer_ID>213</Customer_ID>
		<Customer_Name>Abra Maddox</Customer_Name>
		<Customer_Email>lorem.ut@hotmail.edu</Customer_Email>
		<Customer_Phone>1-770-942-9515</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-25</last_update>
	</record>
	<record>
		<Customer_PK>330</Customer_PK>
		<Customer_ID>397</Customer_ID>
		<Customer_Name>John Alston</Customer_Name>
		<Customer_Email>ipsum@yahoo.org</Customer_Email>
		<Customer_Phone>1-858-179-2781</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-9</last_update>
	</record>
	<record>
		<Customer_PK>331</Customer_PK>
		<Customer_ID>392</Customer_ID>
		<Customer_Name>Remedios Harrell</Customer_Name>
		<Customer_Email>dignissim@outlook.ca</Customer_Email>
		<Customer_Phone>1-951-352-0323</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-26</last_update>
	</record>
	<record>
		<Customer_PK>332</Customer_PK>
		<Customer_ID>95</Customer_ID>
		<Customer_Name>Aristotle Wells</Customer_Name>
		<Customer_Email>auctor.vitae@protonmail.couk</Customer_Email>
		<Customer_Phone>(235) 141-7972</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-21</last_update>
	</record>
	<record>
		<Customer_PK>333</Customer_PK>
		<Customer_ID>285</Customer_ID>
		<Customer_Name>Venus Steele</Customer_Name>
		<Customer_Email>orci@outlook.couk</Customer_Email>
		<Customer_Phone>(811) 498-5611</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-26</last_update>
	</record>
	<record>
		<Customer_PK>334</Customer_PK>
		<Customer_ID>482</Customer_ID>
		<Customer_Name>Bell Levine</Customer_Name>
		<Customer_Email>ligula.aliquam@outlook.org</Customer_Email>
		<Customer_Phone>1-212-715-5782</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-23</last_update>
	</record>
	<record>
		<Customer_PK>335</Customer_PK>
		<Customer_ID>196</Customer_ID>
		<Customer_Name>Perry Anderson</Customer_Name>
		<Customer_Email>turpis.in@aol.org</Customer_Email>
		<Customer_Phone>(648) 561-3224</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-10-31</last_update>
	</record>
	<record>
		<Customer_PK>336</Customer_PK>
		<Customer_ID>231</Customer_ID>
		<Customer_Name>Ulysses Carey</Customer_Name>
		<Customer_Email>faucibus@protonmail.ca</Customer_Email>
		<Customer_Phone>(233) 458-8212</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-9</last_update>
	</record>
	<record>
		<Customer_PK>337</Customer_PK>
		<Customer_ID>48</Customer_ID>
		<Customer_Name>Quemby Barnes</Customer_Name>
		<Customer_Email>vel.est@protonmail.edu</Customer_Email>
		<Customer_Phone>(302) 384-5127</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-5</last_update>
	</record>
	<record>
		<Customer_PK>338</Customer_PK>
		<Customer_ID>349</Customer_ID>
		<Customer_Name>Barclay Sparks</Customer_Name>
		<Customer_Email>rhoncus.id@google.com</Customer_Email>
		<Customer_Phone>(438) 607-3022</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-8</last_update>
	</record>
	<record>
		<Customer_PK>339</Customer_PK>
		<Customer_ID>436</Customer_ID>
		<Customer_Name>Brock Cooley</Customer_Name>
		<Customer_Email>quis.pede@protonmail.net</Customer_Email>
		<Customer_Phone>(442) 555-2644</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-22</last_update>
	</record>
	<record>
		<Customer_PK>340</Customer_PK>
		<Customer_ID>29</Customer_ID>
		<Customer_Name>Imani Underwood</Customer_Name>
		<Customer_Email>suspendisse@icloud.ca</Customer_Email>
		<Customer_Phone>1-873-699-7561</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-13</last_update>
	</record>
	<record>
		<Customer_PK>341</Customer_PK>
		<Customer_ID>400</Customer_ID>
		<Customer_Name>Amaya Reynolds</Customer_Name>
		<Customer_Email>sollicitudin.commodo@hotmail.org</Customer_Email>
		<Customer_Phone>1-360-972-6285</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-2-8</last_update>
	</record>
	<record>
		<Customer_PK>342</Customer_PK>
		<Customer_ID>488</Customer_ID>
		<Customer_Name>Brett Buckner</Customer_Name>
		<Customer_Email>mauris.non.dui@hotmail.net</Customer_Email>
		<Customer_Phone>(235) 825-4267</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-1</last_update>
	</record>
	<record>
		<Customer_PK>343</Customer_PK>
		<Customer_ID>330</Customer_ID>
		<Customer_Name>Murphy Sullivan</Customer_Name>
		<Customer_Email>litora@google.net</Customer_Email>
		<Customer_Phone>(788) 650-1615</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-16</last_update>
	</record>
	<record>
		<Customer_PK>344</Customer_PK>
		<Customer_ID>370</Customer_ID>
		<Customer_Name>Shelby Ochoa</Customer_Name>
		<Customer_Email>enim.commodo.hendrerit@hotmail.org</Customer_Email>
		<Customer_Phone>1-466-961-7685</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-11-3</last_update>
	</record>
	<record>
		<Customer_PK>345</Customer_PK>
		<Customer_ID>55</Customer_ID>
		<Customer_Name>Alice Cooley</Customer_Name>
		<Customer_Email>risus.quisque.libero@yahoo.net</Customer_Email>
		<Customer_Phone>1-485-608-8795</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-7</last_update>
	</record>
	<record>
		<Customer_PK>346</Customer_PK>
		<Customer_ID>316</Customer_ID>
		<Customer_Name>Kasper Mccarthy</Customer_Name>
		<Customer_Email>pellentesque.tellus.sem@protonmail.org</Customer_Email>
		<Customer_Phone>(955) 458-1727</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-22</last_update>
	</record>
	<record>
		<Customer_PK>347</Customer_PK>
		<Customer_ID>367</Customer_ID>
		<Customer_Name>Macy Whitaker</Customer_Name>
		<Customer_Email>purus@icloud.edu</Customer_Email>
		<Customer_Phone>1-797-680-0156</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-1</last_update>
	</record>
	<record>
		<Customer_PK>348</Customer_PK>
		<Customer_ID>117</Customer_ID>
		<Customer_Name>Macey Boyer</Customer_Name>
		<Customer_Email>nisl.nulla@icloud.org</Customer_Email>
		<Customer_Phone>1-331-828-2151</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-8-15</last_update>
	</record>
	<record>
		<Customer_PK>349</Customer_PK>
		<Customer_ID>423</Customer_ID>
		<Customer_Name>Naomi Hunter</Customer_Name>
		<Customer_Email>eu.sem@google.org</Customer_Email>
		<Customer_Phone>1-116-374-8621</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-18</last_update>
	</record>
	<record>
		<Customer_PK>350</Customer_PK>
		<Customer_ID>159</Customer_ID>
		<Customer_Name>Liberty Lancaster</Customer_Name>
		<Customer_Email>nonummy.fusce.fermentum@hotmail.edu</Customer_Email>
		<Customer_Phone>1-728-632-8790</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-3</last_update>
	</record>
	<record>
		<Customer_PK>351</Customer_PK>
		<Customer_ID>130</Customer_ID>
		<Customer_Name>Nolan Hogan</Customer_Name>
		<Customer_Email>tempus.lorem.fringilla@icloud.edu</Customer_Email>
		<Customer_Phone>1-264-247-3345</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-24</last_update>
	</record>
	<record>
		<Customer_PK>352</Customer_PK>
		<Customer_ID>434</Customer_ID>
		<Customer_Name>Nigel Parker</Customer_Name>
		<Customer_Email>luctus.et.ultrices@aol.net</Customer_Email>
		<Customer_Phone>1-397-531-5953</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-12</last_update>
	</record>
	<record>
		<Customer_PK>353</Customer_PK>
		<Customer_ID>347</Customer_ID>
		<Customer_Name>Sopoline Parker</Customer_Name>
		<Customer_Email>mi.ac.mattis@hotmail.couk</Customer_Email>
		<Customer_Phone>(242) 646-7962</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-29</last_update>
	</record>
	<record>
		<Customer_PK>354</Customer_PK>
		<Customer_ID>452</Customer_ID>
		<Customer_Name>Melanie Ford</Customer_Name>
		<Customer_Email>eget.metus@outlook.ca</Customer_Email>
		<Customer_Phone>(685) 177-1053</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-5-4</last_update>
	</record>
	<record>
		<Customer_PK>355</Customer_PK>
		<Customer_ID>278</Customer_ID>
		<Customer_Name>Jelani Mitchell</Customer_Name>
		<Customer_Email>gravida.nunc.sed@google.org</Customer_Email>
		<Customer_Phone>(336) 260-5085</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-5-3</last_update>
	</record>
	<record>
		<Customer_PK>356</Customer_PK>
		<Customer_ID>144</Customer_ID>
		<Customer_Name>Jocelyn Weiss</Customer_Name>
		<Customer_Email>faucibus@yahoo.couk</Customer_Email>
		<Customer_Phone>1-227-885-5461</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-7</last_update>
	</record>
	<record>
		<Customer_PK>357</Customer_PK>
		<Customer_ID>301</Customer_ID>
		<Customer_Name>Alden Johnson</Customer_Name>
		<Customer_Email>aliquet.lobortis@yahoo.ca</Customer_Email>
		<Customer_Phone>(348) 689-4557</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-2</last_update>
	</record>
	<record>
		<Customer_PK>358</Customer_PK>
		<Customer_ID>99</Customer_ID>
		<Customer_Name>Laurel Barnett</Customer_Name>
		<Customer_Email>nec.leo@google.org</Customer_Email>
		<Customer_Phone>1-763-612-0148</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-28</last_update>
	</record>
	<record>
		<Customer_PK>359</Customer_PK>
		<Customer_ID>98</Customer_ID>
		<Customer_Name>Joseph Morris</Customer_Name>
		<Customer_Email>ornare.sagittis@hotmail.ca</Customer_Email>
		<Customer_Phone>(695) 857-4709</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-18</last_update>
	</record>
	<record>
		<Customer_PK>360</Customer_PK>
		<Customer_ID>36</Customer_ID>
		<Customer_Name>Aladdin Bird</Customer_Name>
		<Customer_Email>gravida.sit@yahoo.com</Customer_Email>
		<Customer_Phone>1-582-287-7937</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-31</last_update>
	</record>
	<record>
		<Customer_PK>361</Customer_PK>
		<Customer_ID>379</Customer_ID>
		<Customer_Name>Harlan Green</Customer_Name>
		<Customer_Email>sit.amet.dapibus@yahoo.net</Customer_Email>
		<Customer_Phone>(579) 821-7706</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-19</last_update>
	</record>
	<record>
		<Customer_PK>362</Customer_PK>
		<Customer_ID>37</Customer_ID>
		<Customer_Name>Ali Robles</Customer_Name>
		<Customer_Email>ac.turpis@hotmail.couk</Customer_Email>
		<Customer_Phone>1-332-716-8348</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-17</last_update>
	</record>
	<record>
		<Customer_PK>363</Customer_PK>
		<Customer_ID>354</Customer_ID>
		<Customer_Name>Aline Williams</Customer_Name>
		<Customer_Email>vulputate@google.ca</Customer_Email>
		<Customer_Phone>1-539-622-6148</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-2</last_update>
	</record>
	<record>
		<Customer_PK>364</Customer_PK>
		<Customer_ID>401</Customer_ID>
		<Customer_Name>Tad Finch</Customer_Name>
		<Customer_Email>scelerisque.neque.sed@protonmail.edu</Customer_Email>
		<Customer_Phone>1-464-544-9642</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-16</last_update>
	</record>
	<record>
		<Customer_PK>365</Customer_PK>
		<Customer_ID>167</Customer_ID>
		<Customer_Name>Craig Santos</Customer_Name>
		<Customer_Email>congue@hotmail.couk</Customer_Email>
		<Customer_Phone>1-730-425-1081</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-9-16</last_update>
	</record>
	<record>
		<Customer_PK>366</Customer_PK>
		<Customer_ID>459</Customer_ID>
		<Customer_Name>Uriel Simmons</Customer_Name>
		<Customer_Email>etiam@icloud.com</Customer_Email>
		<Customer_Phone>(861) 261-3882</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-15</last_update>
	</record>
	<record>
		<Customer_PK>367</Customer_PK>
		<Customer_ID>157</Customer_ID>
		<Customer_Name>Dillon Leonard</Customer_Name>
		<Customer_Email>dapibus.gravida@icloud.com</Customer_Email>
		<Customer_Phone>(725) 887-6446</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-9-7</last_update>
	</record>
	<record>
		<Customer_PK>368</Customer_PK>
		<Customer_ID>93</Customer_ID>
		<Customer_Name>Jackson George</Customer_Name>
		<Customer_Email>dictum.proin@hotmail.org</Customer_Email>
		<Customer_Phone>1-231-809-8258</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-12</last_update>
	</record>
	<record>
		<Customer_PK>369</Customer_PK>
		<Customer_ID>118</Customer_ID>
		<Customer_Name>Hedley Glenn</Customer_Name>
		<Customer_Email>vulputate@yahoo.net</Customer_Email>
		<Customer_Phone>1-657-347-3678</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-8-27</last_update>
	</record>
	<record>
		<Customer_PK>370</Customer_PK>
		<Customer_ID>149</Customer_ID>
		<Customer_Name>Emerald Romero</Customer_Name>
		<Customer_Email>nibh.vulputate.mauris@protonmail.org</Customer_Email>
		<Customer_Phone>(868) 755-1824</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-8-15</last_update>
	</record>
	<record>
		<Customer_PK>371</Customer_PK>
		<Customer_ID>493</Customer_ID>
		<Customer_Name>Calista Vargas</Customer_Name>
		<Customer_Email>ac.eleifend@yahoo.edu</Customer_Email>
		<Customer_Phone>1-611-883-2324</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-11-10</last_update>
	</record>
	<record>
		<Customer_PK>372</Customer_PK>
		<Customer_ID>423</Customer_ID>
		<Customer_Name>Bernard Poole</Customer_Name>
		<Customer_Email>vulputate.dui@icloud.ca</Customer_Email>
		<Customer_Phone>(237) 927-3164</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-21</last_update>
	</record>
	<record>
		<Customer_PK>373</Customer_PK>
		<Customer_ID>170</Customer_ID>
		<Customer_Name>Phillip Joyner</Customer_Name>
		<Customer_Email>lectus.pede.ultrices@icloud.net</Customer_Email>
		<Customer_Phone>1-245-438-9506</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-7</last_update>
	</record>
	<record>
		<Customer_PK>374</Customer_PK>
		<Customer_ID>231</Customer_ID>
		<Customer_Name>Daria Cabrera</Customer_Name>
		<Customer_Email>quisque.imperdiet@outlook.org</Customer_Email>
		<Customer_Phone>(816) 337-7145</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-9</last_update>
	</record>
	<record>
		<Customer_PK>375</Customer_PK>
		<Customer_ID>356</Customer_ID>
		<Customer_Name>Courtney Cook</Customer_Name>
		<Customer_Email>massa.vestibulum@icloud.org</Customer_Email>
		<Customer_Phone>(354) 538-4225</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-21</last_update>
	</record>
	<record>
		<Customer_PK>376</Customer_PK>
		<Customer_ID>253</Customer_ID>
		<Customer_Name>Josephine Williamson</Customer_Name>
		<Customer_Email>integer@google.net</Customer_Email>
		<Customer_Phone>1-861-234-4791</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-1-8</last_update>
	</record>
	<record>
		<Customer_PK>377</Customer_PK>
		<Customer_ID>397</Customer_ID>
		<Customer_Name>September Valencia</Customer_Name>
		<Customer_Email>non.lorem.vitae@protonmail.org</Customer_Email>
		<Customer_Phone>1-565-571-4371</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-26</last_update>
	</record>
	<record>
		<Customer_PK>378</Customer_PK>
		<Customer_ID>206</Customer_ID>
		<Customer_Name>Judah Hart</Customer_Name>
		<Customer_Email>ornare@aol.ca</Customer_Email>
		<Customer_Phone>(453) 343-5480</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-11-7</last_update>
	</record>
	<record>
		<Customer_PK>379</Customer_PK>
		<Customer_ID>150</Customer_ID>
		<Customer_Name>Hasad Porter</Customer_Name>
		<Customer_Email>nascetur.ridiculus@protonmail.ca</Customer_Email>
		<Customer_Phone>(942) 971-3134</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-17</last_update>
	</record>
	<record>
		<Customer_PK>380</Customer_PK>
		<Customer_ID>344</Customer_ID>
		<Customer_Name>Dominique Mercer</Customer_Name>
		<Customer_Email>nostra.per@protonmail.ca</Customer_Email>
		<Customer_Phone>(724) 730-7662</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-7</last_update>
	</record>
	<record>
		<Customer_PK>381</Customer_PK>
		<Customer_ID>412</Customer_ID>
		<Customer_Name>Zahir Small</Customer_Name>
		<Customer_Email>cursus.nunc@aol.ca</Customer_Email>
		<Customer_Phone>1-482-719-2478</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-1</last_update>
	</record>
	<record>
		<Customer_PK>382</Customer_PK>
		<Customer_ID>83</Customer_ID>
		<Customer_Name>Ralph Hoffman</Customer_Name>
		<Customer_Email>quisque@google.org</Customer_Email>
		<Customer_Phone>1-251-356-0642</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-10-5</last_update>
	</record>
	<record>
		<Customer_PK>383</Customer_PK>
		<Customer_ID>478</Customer_ID>
		<Customer_Name>Gillian Emerson</Customer_Name>
		<Customer_Email>cursus.vestibulum@aol.com</Customer_Email>
		<Customer_Phone>1-777-241-6937</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-6</last_update>
	</record>
	<record>
		<Customer_PK>384</Customer_PK>
		<Customer_ID>134</Customer_ID>
		<Customer_Name>Jonah Dorsey</Customer_Name>
		<Customer_Email>eros.nam.consequat@aol.edu</Customer_Email>
		<Customer_Phone>(529) 574-6275</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-9-15</last_update>
	</record>
	<record>
		<Customer_PK>385</Customer_PK>
		<Customer_ID>214</Customer_ID>
		<Customer_Name>Basil Bird</Customer_Name>
		<Customer_Email>nulla@outlook.couk</Customer_Email>
		<Customer_Phone>(401) 346-7827</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-12</last_update>
	</record>
	<record>
		<Customer_PK>386</Customer_PK>
		<Customer_ID>76</Customer_ID>
		<Customer_Name>Cherokee Bryant</Customer_Name>
		<Customer_Email>sed@protonmail.edu</Customer_Email>
		<Customer_Phone>1-288-497-4953</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-13</last_update>
	</record>
	<record>
		<Customer_PK>387</Customer_PK>
		<Customer_ID>157</Customer_ID>
		<Customer_Name>Benedict Mcneil</Customer_Name>
		<Customer_Email>aenean@outlook.edu</Customer_Email>
		<Customer_Phone>(973) 473-4992</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-13</last_update>
	</record>
	<record>
		<Customer_PK>388</Customer_PK>
		<Customer_ID>185</Customer_ID>
		<Customer_Name>Lamar Acevedo</Customer_Name>
		<Customer_Email>libero@outlook.couk</Customer_Email>
		<Customer_Phone>(498) 732-6548</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-13</last_update>
	</record>
	<record>
		<Customer_PK>389</Customer_PK>
		<Customer_ID>94</Customer_ID>
		<Customer_Name>Chandler Weber</Customer_Name>
		<Customer_Email>in@google.net</Customer_Email>
		<Customer_Phone>1-235-673-1162</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-19</last_update>
	</record>
	<record>
		<Customer_PK>390</Customer_PK>
		<Customer_ID>403</Customer_ID>
		<Customer_Name>Dillon Sargent</Customer_Name>
		<Customer_Email>nunc.ac.mattis@hotmail.ca</Customer_Email>
		<Customer_Phone>1-934-721-5779</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-5</last_update>
	</record>
	<record>
		<Customer_PK>391</Customer_PK>
		<Customer_ID>158</Customer_ID>
		<Customer_Name>Priscilla Mcfadden</Customer_Name>
		<Customer_Email>posuere.vulputate@icloud.ca</Customer_Email>
		<Customer_Phone>1-262-220-7963</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-17</last_update>
	</record>
	<record>
		<Customer_PK>392</Customer_PK>
		<Customer_ID>308</Customer_ID>
		<Customer_Name>Riley Harper</Customer_Name>
		<Customer_Email>velit.cras.lorem@yahoo.com</Customer_Email>
		<Customer_Phone>1-323-788-2542</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-24</last_update>
	</record>
	<record>
		<Customer_PK>393</Customer_PK>
		<Customer_ID>136</Customer_ID>
		<Customer_Name>Kylee Potts</Customer_Name>
		<Customer_Email>sit@icloud.edu</Customer_Email>
		<Customer_Phone>1-475-241-5688</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-30</last_update>
	</record>
	<record>
		<Customer_PK>394</Customer_PK>
		<Customer_ID>286</Customer_ID>
		<Customer_Name>Jescie Farley</Customer_Name>
		<Customer_Email>lacus.ut.nec@outlook.couk</Customer_Email>
		<Customer_Phone>1-333-859-5366</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-9-30</last_update>
	</record>
	<record>
		<Customer_PK>395</Customer_PK>
		<Customer_ID>233</Customer_ID>
		<Customer_Name>Bethany Harper</Customer_Name>
		<Customer_Email>dignissim.lacus.aliquam@aol.couk</Customer_Email>
		<Customer_Phone>1-429-950-5822</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-6</last_update>
	</record>
	<record>
		<Customer_PK>396</Customer_PK>
		<Customer_ID>481</Customer_ID>
		<Customer_Name>Hanae Aguirre</Customer_Name>
		<Customer_Email>nullam@aol.ca</Customer_Email>
		<Customer_Phone>1-661-110-4591</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-26</last_update>
	</record>
	<record>
		<Customer_PK>397</Customer_PK>
		<Customer_ID>88</Customer_ID>
		<Customer_Name>Deacon Ferguson</Customer_Name>
		<Customer_Email>eu.nibh@google.net</Customer_Email>
		<Customer_Phone>(663) 146-1721</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-11</last_update>
	</record>
	<record>
		<Customer_PK>398</Customer_PK>
		<Customer_ID>26</Customer_ID>
		<Customer_Name>Andrew Poole</Customer_Name>
		<Customer_Email>sed.leo.cras@aol.edu</Customer_Email>
		<Customer_Phone>1-953-487-0333</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-27</last_update>
	</record>
	<record>
		<Customer_PK>399</Customer_PK>
		<Customer_ID>129</Customer_ID>
		<Customer_Name>Reed Dale</Customer_Name>
		<Customer_Email>tristique.neque.venenatis@aol.couk</Customer_Email>
		<Customer_Phone>1-578-809-1111</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-18</last_update>
	</record>
	<record>
		<Customer_PK>400</Customer_PK>
		<Customer_ID>90</Customer_ID>
		<Customer_Name>Dominique Rodgers</Customer_Name>
		<Customer_Email>et@outlook.edu</Customer_Email>
		<Customer_Phone>(151) 318-4627</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-28</last_update>
	</record>
	<record>
		<Customer_PK>401</Customer_PK>
		<Customer_ID>137</Customer_ID>
		<Customer_Name>Brendan Donovan</Customer_Name>
		<Customer_Email>sit@yahoo.net</Customer_Email>
		<Customer_Phone>(377) 303-1150</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-29</last_update>
	</record>
	<record>
		<Customer_PK>402</Customer_PK>
		<Customer_ID>217</Customer_ID>
		<Customer_Name>Nyssa Landry</Customer_Name>
		<Customer_Email>integer@hotmail.net</Customer_Email>
		<Customer_Phone>(612) 848-1656</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-24</last_update>
	</record>
	<record>
		<Customer_PK>403</Customer_PK>
		<Customer_ID>164</Customer_ID>
		<Customer_Name>Calista Castaneda</Customer_Name>
		<Customer_Email>risus@protonmail.org</Customer_Email>
		<Customer_Phone>1-643-303-1446</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-6</last_update>
	</record>
	<record>
		<Customer_PK>404</Customer_PK>
		<Customer_ID>248</Customer_ID>
		<Customer_Name>Patience Conway</Customer_Name>
		<Customer_Email>nisl@hotmail.com</Customer_Email>
		<Customer_Phone>(227) 953-8458</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-2</last_update>
	</record>
	<record>
		<Customer_PK>405</Customer_PK>
		<Customer_ID>270</Customer_ID>
		<Customer_Name>Emery Garrett</Customer_Name>
		<Customer_Email>sit@google.com</Customer_Email>
		<Customer_Phone>1-305-134-3131</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-10-2</last_update>
	</record>
	<record>
		<Customer_PK>406</Customer_PK>
		<Customer_ID>417</Customer_ID>
		<Customer_Name>Rosalyn Barrett</Customer_Name>
		<Customer_Email>aliquet.lobortis.nisi@yahoo.edu</Customer_Email>
		<Customer_Phone>(533) 441-6783</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-27</last_update>
	</record>
	<record>
		<Customer_PK>407</Customer_PK>
		<Customer_ID>73</Customer_ID>
		<Customer_Name>Azalia Foreman</Customer_Name>
		<Customer_Email>sodales.mauris.blandit@outlook.ca</Customer_Email>
		<Customer_Phone>(826) 326-6402</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-1-8</last_update>
	</record>
	<record>
		<Customer_PK>408</Customer_PK>
		<Customer_ID>435</Customer_ID>
		<Customer_Name>Lillith Simmons</Customer_Name>
		<Customer_Email>ac.risus@aol.ca</Customer_Email>
		<Customer_Phone>1-206-827-4498</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-27</last_update>
	</record>
	<record>
		<Customer_PK>409</Customer_PK>
		<Customer_ID>243</Customer_ID>
		<Customer_Name>Jacqueline Salinas</Customer_Name>
		<Customer_Email>id.risus.quis@hotmail.edu</Customer_Email>
		<Customer_Phone>(486) 927-4608</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-5-12</last_update>
	</record>
	<record>
		<Customer_PK>410</Customer_PK>
		<Customer_ID>2</Customer_ID>
		<Customer_Name>Jennifer Ratliff</Customer_Name>
		<Customer_Email>ut@hotmail.com</Customer_Email>
		<Customer_Phone>(610) 506-3687</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-3</last_update>
	</record>
	<record>
		<Customer_PK>411</Customer_PK>
		<Customer_ID>366</Customer_ID>
		<Customer_Name>Idola George</Customer_Name>
		<Customer_Email>magna.et@hotmail.org</Customer_Email>
		<Customer_Phone>(713) 379-3508</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-30</last_update>
	</record>
	<record>
		<Customer_PK>412</Customer_PK>
		<Customer_ID>336</Customer_ID>
		<Customer_Name>Giacomo Black</Customer_Name>
		<Customer_Email>ac.risus.morbi@aol.edu</Customer_Email>
		<Customer_Phone>1-351-331-8833</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-23</last_update>
	</record>
	<record>
		<Customer_PK>413</Customer_PK>
		<Customer_ID>418</Customer_ID>
		<Customer_Name>Damian Padilla</Customer_Name>
		<Customer_Email>ad@hotmail.ca</Customer_Email>
		<Customer_Phone>1-316-312-6481</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-27</last_update>
	</record>
	<record>
		<Customer_PK>414</Customer_PK>
		<Customer_ID>155</Customer_ID>
		<Customer_Name>Rebekah Knapp</Customer_Name>
		<Customer_Email>quisque@outlook.org</Customer_Email>
		<Customer_Phone>1-796-624-4615</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-5</last_update>
	</record>
	<record>
		<Customer_PK>415</Customer_PK>
		<Customer_ID>77</Customer_ID>
		<Customer_Name>Baker Cash</Customer_Name>
		<Customer_Email>sed.dui@icloud.couk</Customer_Email>
		<Customer_Phone>1-773-794-7573</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-21</last_update>
	</record>
	<record>
		<Customer_PK>416</Customer_PK>
		<Customer_ID>203</Customer_ID>
		<Customer_Name>Martena Barnett</Customer_Name>
		<Customer_Email>elit.fermentum.risus@hotmail.net</Customer_Email>
		<Customer_Phone>1-722-224-5150</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-28</last_update>
	</record>
	<record>
		<Customer_PK>417</Customer_PK>
		<Customer_ID>341</Customer_ID>
		<Customer_Name>Judah Guerrero</Customer_Name>
		<Customer_Email>massa.integer@icloud.couk</Customer_Email>
		<Customer_Phone>1-213-210-8235</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-2-6</last_update>
	</record>
	<record>
		<Customer_PK>418</Customer_PK>
		<Customer_ID>337</Customer_ID>
		<Customer_Name>Reed Sears</Customer_Name>
		<Customer_Email>in@yahoo.couk</Customer_Email>
		<Customer_Phone>(458) 243-4282</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-17</last_update>
	</record>
	<record>
		<Customer_PK>419</Customer_PK>
		<Customer_ID>174</Customer_ID>
		<Customer_Name>Britanni Tillman</Customer_Name>
		<Customer_Email>tempus.mauris@aol.couk</Customer_Email>
		<Customer_Phone>1-877-875-9273</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-5-9</last_update>
	</record>
	<record>
		<Customer_PK>420</Customer_PK>
		<Customer_ID>168</Customer_ID>
		<Customer_Name>Kirsten Richardson</Customer_Name>
		<Customer_Email>eget.massa@yahoo.edu</Customer_Email>
		<Customer_Phone>(727) 877-7735</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-16</last_update>
	</record>
	<record>
		<Customer_PK>421</Customer_PK>
		<Customer_ID>256</Customer_ID>
		<Customer_Name>Owen Brooks</Customer_Name>
		<Customer_Email>proin.velit@icloud.com</Customer_Email>
		<Customer_Phone>1-664-426-0710</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-17</last_update>
	</record>
	<record>
		<Customer_PK>422</Customer_PK>
		<Customer_ID>274</Customer_ID>
		<Customer_Name>Leila Sloan</Customer_Name>
		<Customer_Email>cubilia@yahoo.net</Customer_Email>
		<Customer_Phone>(295) 165-6827</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-21</last_update>
	</record>
	<record>
		<Customer_PK>423</Customer_PK>
		<Customer_ID>347</Customer_ID>
		<Customer_Name>Ayanna Stanton</Customer_Name>
		<Customer_Email>cursus.et.magna@aol.org</Customer_Email>
		<Customer_Phone>1-160-978-8289</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-9-26</last_update>
	</record>
	<record>
		<Customer_PK>424</Customer_PK>
		<Customer_ID>20</Customer_ID>
		<Customer_Name>Quinlan Strong</Customer_Name>
		<Customer_Email>magna.et@hotmail.ca</Customer_Email>
		<Customer_Phone>1-525-745-5121</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-2</last_update>
	</record>
	<record>
		<Customer_PK>425</Customer_PK>
		<Customer_ID>192</Customer_ID>
		<Customer_Name>Amber Prince</Customer_Name>
		<Customer_Email>elementum.at@outlook.net</Customer_Email>
		<Customer_Phone>1-675-575-3504</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-5</last_update>
	</record>
	<record>
		<Customer_PK>426</Customer_PK>
		<Customer_ID>214</Customer_ID>
		<Customer_Name>Gloria Lee</Customer_Name>
		<Customer_Email>feugiat.metus@icloud.org</Customer_Email>
		<Customer_Phone>1-845-515-4382</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-9-18</last_update>
	</record>
	<record>
		<Customer_PK>427</Customer_PK>
		<Customer_ID>35</Customer_ID>
		<Customer_Name>Camden House</Customer_Name>
		<Customer_Email>morbi.metus@outlook.net</Customer_Email>
		<Customer_Phone>(617) 508-9563</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-7</last_update>
	</record>
	<record>
		<Customer_PK>428</Customer_PK>
		<Customer_ID>14</Customer_ID>
		<Customer_Name>Hermione Cain</Customer_Name>
		<Customer_Email>vulputate.risus.a@yahoo.edu</Customer_Email>
		<Customer_Phone>1-976-867-5957</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-9</last_update>
	</record>
	<record>
		<Customer_PK>429</Customer_PK>
		<Customer_ID>238</Customer_ID>
		<Customer_Name>Hanae Valencia</Customer_Name>
		<Customer_Email>libero@outlook.net</Customer_Email>
		<Customer_Phone>1-654-421-4197</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-4-13</last_update>
	</record>
	<record>
		<Customer_PK>430</Customer_PK>
		<Customer_ID>51</Customer_ID>
		<Customer_Name>Yoshi Mcmahon</Customer_Name>
		<Customer_Email>in.ornare@icloud.com</Customer_Email>
		<Customer_Phone>(517) 224-8763</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-14</last_update>
	</record>
	<record>
		<Customer_PK>431</Customer_PK>
		<Customer_ID>237</Customer_ID>
		<Customer_Name>Bethany Boyer</Customer_Name>
		<Customer_Email>a.aliquet@protonmail.org</Customer_Email>
		<Customer_Phone>(886) 964-6468</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-8-26</last_update>
	</record>
	<record>
		<Customer_PK>432</Customer_PK>
		<Customer_ID>313</Customer_ID>
		<Customer_Name>Xenos Roman</Customer_Name>
		<Customer_Email>vestibulum.ante@yahoo.com</Customer_Email>
		<Customer_Phone>1-576-479-4318</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-21</last_update>
	</record>
	<record>
		<Customer_PK>433</Customer_PK>
		<Customer_ID>112</Customer_ID>
		<Customer_Name>Jesse Knowles</Customer_Name>
		<Customer_Email>magna.phasellus.dolor@yahoo.com</Customer_Email>
		<Customer_Phone>(451) 177-1573</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-10</last_update>
	</record>
	<record>
		<Customer_PK>434</Customer_PK>
		<Customer_ID>37</Customer_ID>
		<Customer_Name>Nichole Ruiz</Customer_Name>
		<Customer_Email>nostra.per@outlook.edu</Customer_Email>
		<Customer_Phone>(573) 741-7931</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-11-27</last_update>
	</record>
	<record>
		<Customer_PK>435</Customer_PK>
		<Customer_ID>226</Customer_ID>
		<Customer_Name>Mari Pruitt</Customer_Name>
		<Customer_Email>eros.non.enim@aol.couk</Customer_Email>
		<Customer_Phone>(511) 831-7662</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-20</last_update>
	</record>
	<record>
		<Customer_PK>436</Customer_PK>
		<Customer_ID>93</Customer_ID>
		<Customer_Name>Justine Morrow</Customer_Name>
		<Customer_Email>ut.ipsum.ac@hotmail.com</Customer_Email>
		<Customer_Phone>(751) 815-1652</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-30</last_update>
	</record>
	<record>
		<Customer_PK>437</Customer_PK>
		<Customer_ID>174</Customer_ID>
		<Customer_Name>Karen Lane</Customer_Name>
		<Customer_Email>erat.semper@outlook.com</Customer_Email>
		<Customer_Phone>(572) 766-1101</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-25</last_update>
	</record>
	<record>
		<Customer_PK>438</Customer_PK>
		<Customer_ID>96</Customer_ID>
		<Customer_Name>Justin Meyers</Customer_Name>
		<Customer_Email>pharetra.felis@hotmail.net</Customer_Email>
		<Customer_Phone>1-876-522-4432</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-22</last_update>
	</record>
	<record>
		<Customer_PK>439</Customer_PK>
		<Customer_ID>167</Customer_ID>
		<Customer_Name>Adrienne Head</Customer_Name>
		<Customer_Email>faucibus@google.com</Customer_Email>
		<Customer_Phone>1-775-599-1836</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-14</last_update>
	</record>
	<record>
		<Customer_PK>440</Customer_PK>
		<Customer_ID>126</Customer_ID>
		<Customer_Name>Joseph May</Customer_Name>
		<Customer_Email>justo.eu.arcu@yahoo.org</Customer_Email>
		<Customer_Phone>(111) 316-8243</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-21</last_update>
	</record>
	<record>
		<Customer_PK>441</Customer_PK>
		<Customer_ID>471</Customer_ID>
		<Customer_Name>Patricia Bruce</Customer_Name>
		<Customer_Email>augue@hotmail.com</Customer_Email>
		<Customer_Phone>(629) 157-4344</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-14</last_update>
	</record>
	<record>
		<Customer_PK>442</Customer_PK>
		<Customer_ID>199</Customer_ID>
		<Customer_Name>Abraham Benton</Customer_Name>
		<Customer_Email>vestibulum@protonmail.net</Customer_Email>
		<Customer_Phone>(115) 805-3187</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-11</last_update>
	</record>
	<record>
		<Customer_PK>443</Customer_PK>
		<Customer_ID>15</Customer_ID>
		<Customer_Name>Clare Henry</Customer_Name>
		<Customer_Email>blandit.viverra.donec@outlook.net</Customer_Email>
		<Customer_Phone>1-813-770-6064</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-9-18</last_update>
	</record>
	<record>
		<Customer_PK>444</Customer_PK>
		<Customer_ID>90</Customer_ID>
		<Customer_Name>Nell Hansen</Customer_Name>
		<Customer_Email>auctor.vitae@hotmail.edu</Customer_Email>
		<Customer_Phone>1-849-915-3764</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-17</last_update>
	</record>
	<record>
		<Customer_PK>445</Customer_PK>
		<Customer_ID>462</Customer_ID>
		<Customer_Name>Veronica Gould</Customer_Name>
		<Customer_Email>duis.sit@outlook.com</Customer_Email>
		<Customer_Phone>(746) 346-6113</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-9</last_update>
	</record>
	<record>
		<Customer_PK>446</Customer_PK>
		<Customer_ID>489</Customer_ID>
		<Customer_Name>Fiona Fowler</Customer_Name>
		<Customer_Email>urna@yahoo.couk</Customer_Email>
		<Customer_Phone>(297) 738-0322</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-27</last_update>
	</record>
	<record>
		<Customer_PK>447</Customer_PK>
		<Customer_ID>490</Customer_ID>
		<Customer_Name>Craig Mason</Customer_Name>
		<Customer_Email>purus.duis@icloud.edu</Customer_Email>
		<Customer_Phone>1-388-165-1568</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-9-28</last_update>
	</record>
	<record>
		<Customer_PK>448</Customer_PK>
		<Customer_ID>89</Customer_ID>
		<Customer_Name>Rinah Ware</Customer_Name>
		<Customer_Email>libero@yahoo.ca</Customer_Email>
		<Customer_Phone>(829) 382-5937</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-2</last_update>
	</record>
	<record>
		<Customer_PK>449</Customer_PK>
		<Customer_ID>123</Customer_ID>
		<Customer_Name>Maris Chang</Customer_Name>
		<Customer_Email>tempor@outlook.ca</Customer_Email>
		<Customer_Phone>(826) 847-6402</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-9-24</last_update>
	</record>
	<record>
		<Customer_PK>450</Customer_PK>
		<Customer_ID>156</Customer_ID>
		<Customer_Name>Carly Mitchell</Customer_Name>
		<Customer_Email>vitae.dolor.donec@hotmail.edu</Customer_Email>
		<Customer_Phone>1-933-588-6263</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-9</last_update>
	</record>
	<record>
		<Customer_PK>451</Customer_PK>
		<Customer_ID>387</Customer_ID>
		<Customer_Name>Chelsea Reese</Customer_Name>
		<Customer_Email>vestibulum@google.net</Customer_Email>
		<Customer_Phone>(843) 952-1175</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-16</last_update>
	</record>
	<record>
		<Customer_PK>452</Customer_PK>
		<Customer_ID>336</Customer_ID>
		<Customer_Name>Logan Weaver</Customer_Name>
		<Customer_Email>eu.tempor@yahoo.ca</Customer_Email>
		<Customer_Phone>(237) 736-6681</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-2</last_update>
	</record>
	<record>
		<Customer_PK>453</Customer_PK>
		<Customer_ID>224</Customer_ID>
		<Customer_Name>Charde Livingston</Customer_Name>
		<Customer_Email>vulputate.lacus@protonmail.com</Customer_Email>
		<Customer_Phone>(414) 204-3525</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-8-25</last_update>
	</record>
	<record>
		<Customer_PK>454</Customer_PK>
		<Customer_ID>386</Customer_ID>
		<Customer_Name>Burton Sosa</Customer_Name>
		<Customer_Email>tristique.ac@google.edu</Customer_Email>
		<Customer_Phone>1-987-734-3819</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-12</last_update>
	</record>
	<record>
		<Customer_PK>455</Customer_PK>
		<Customer_ID>16</Customer_ID>
		<Customer_Name>Susan Mcdaniel</Customer_Name>
		<Customer_Email>semper@protonmail.net</Customer_Email>
		<Customer_Phone>1-388-462-7034</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-26</last_update>
	</record>
	<record>
		<Customer_PK>456</Customer_PK>
		<Customer_ID>232</Customer_ID>
		<Customer_Name>Phoebe Pearson</Customer_Name>
		<Customer_Email>montes.nascetur@outlook.edu</Customer_Email>
		<Customer_Phone>(746) 243-5152</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-9-1</last_update>
	</record>
	<record>
		<Customer_PK>457</Customer_PK>
		<Customer_ID>211</Customer_ID>
		<Customer_Name>Fletcher Humphrey</Customer_Name>
		<Customer_Email>neque.nullam@outlook.ca</Customer_Email>
		<Customer_Phone>(578) 584-3302</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-10-20</last_update>
	</record>
	<record>
		<Customer_PK>458</Customer_PK>
		<Customer_ID>101</Customer_ID>
		<Customer_Name>Tanner Pratt</Customer_Name>
		<Customer_Email>at.risus.nunc@outlook.ca</Customer_Email>
		<Customer_Phone>1-822-374-5218</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-1</last_update>
	</record>
	<record>
		<Customer_PK>459</Customer_PK>
		<Customer_ID>24</Customer_ID>
		<Customer_Name>Cameron Sosa</Customer_Name>
		<Customer_Email>et.magnis.dis@aol.couk</Customer_Email>
		<Customer_Phone>1-447-517-3270</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-1-22</last_update>
	</record>
	<record>
		<Customer_PK>460</Customer_PK>
		<Customer_ID>222</Customer_ID>
		<Customer_Name>Mason Green</Customer_Name>
		<Customer_Email>sagittis.lobortis.mauris@yahoo.edu</Customer_Email>
		<Customer_Phone>1-318-344-4846</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-10</last_update>
	</record>
	<record>
		<Customer_PK>461</Customer_PK>
		<Customer_ID>312</Customer_ID>
		<Customer_Name>Amery Owen</Customer_Name>
		<Customer_Email>ullamcorper.eu.euismod@icloud.com</Customer_Email>
		<Customer_Phone>(764) 498-5974</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-24</last_update>
	</record>
	<record>
		<Customer_PK>462</Customer_PK>
		<Customer_ID>147</Customer_ID>
		<Customer_Name>Malcolm Berg</Customer_Name>
		<Customer_Email>mattis.integer@aol.couk</Customer_Email>
		<Customer_Phone>(557) 965-3525</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-31</last_update>
	</record>
	<record>
		<Customer_PK>463</Customer_PK>
		<Customer_ID>395</Customer_ID>
		<Customer_Name>Kamal Fuller</Customer_Name>
		<Customer_Email>consequat@outlook.ca</Customer_Email>
		<Customer_Phone>(411) 356-7986</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-25</last_update>
	</record>
	<record>
		<Customer_PK>464</Customer_PK>
		<Customer_ID>205</Customer_ID>
		<Customer_Name>Karen King</Customer_Name>
		<Customer_Email>dictum.placerat.augue@aol.edu</Customer_Email>
		<Customer_Phone>1-384-742-5032</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-4</last_update>
	</record>
	<record>
		<Customer_PK>465</Customer_PK>
		<Customer_ID>59</Customer_ID>
		<Customer_Name>Nash Wood</Customer_Name>
		<Customer_Email>placerat.augue@hotmail.com</Customer_Email>
		<Customer_Phone>1-778-618-9398</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-27</last_update>
	</record>
	<record>
		<Customer_PK>466</Customer_PK>
		<Customer_ID>163</Customer_ID>
		<Customer_Name>Callie Holden</Customer_Name>
		<Customer_Email>vel.sapien.imperdiet@outlook.net</Customer_Email>
		<Customer_Phone>(784) 302-7164</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-21</last_update>
	</record>
	<record>
		<Customer_PK>467</Customer_PK>
		<Customer_ID>77</Customer_ID>
		<Customer_Name>Lara Black</Customer_Name>
		<Customer_Email>tortor.dictum@aol.com</Customer_Email>
		<Customer_Phone>1-493-919-2864</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-19</last_update>
	</record>
	<record>
		<Customer_PK>468</Customer_PK>
		<Customer_ID>132</Customer_ID>
		<Customer_Name>April Nichols</Customer_Name>
		<Customer_Email>vivamus.sit@protonmail.edu</Customer_Email>
		<Customer_Phone>(195) 417-6704</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-14</last_update>
	</record>
	<record>
		<Customer_PK>469</Customer_PK>
		<Customer_ID>77</Customer_ID>
		<Customer_Name>Forrest Winters</Customer_Name>
		<Customer_Email>donec.consectetuer@outlook.couk</Customer_Email>
		<Customer_Phone>(842) 335-3281</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-8-29</last_update>
	</record>
	<record>
		<Customer_PK>470</Customer_PK>
		<Customer_ID>184</Customer_ID>
		<Customer_Name>Zeus Bailey</Customer_Name>
		<Customer_Email>leo.morbi@hotmail.org</Customer_Email>
		<Customer_Phone>1-247-375-8216</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-8-29</last_update>
	</record>
	<record>
		<Customer_PK>471</Customer_PK>
		<Customer_ID>134</Customer_ID>
		<Customer_Name>Noelle Levy</Customer_Name>
		<Customer_Email>phasellus.dapibus@google.org</Customer_Email>
		<Customer_Phone>1-423-827-1881</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-26</last_update>
	</record>
	<record>
		<Customer_PK>472</Customer_PK>
		<Customer_ID>193</Customer_ID>
		<Customer_Name>Andrew Chase</Customer_Name>
		<Customer_Email>eu.turpis@outlook.couk</Customer_Email>
		<Customer_Phone>(264) 228-5437</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-8</last_update>
	</record>
	<record>
		<Customer_PK>473</Customer_PK>
		<Customer_ID>210</Customer_ID>
		<Customer_Name>Carolyn Haynes</Customer_Name>
		<Customer_Email>vel.mauris@google.com</Customer_Email>
		<Customer_Phone>1-723-863-8964</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-20</last_update>
	</record>
	<record>
		<Customer_PK>474</Customer_PK>
		<Customer_ID>395</Customer_ID>
		<Customer_Name>Risa Walsh</Customer_Name>
		<Customer_Email>nulla.eu.neque@outlook.ca</Customer_Email>
		<Customer_Phone>(104) 638-7385</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-26</last_update>
	</record>
	<record>
		<Customer_PK>475</Customer_PK>
		<Customer_ID>247</Customer_ID>
		<Customer_Name>Mikayla Pittman</Customer_Name>
		<Customer_Email>consectetuer.ipsum.nunc@hotmail.edu</Customer_Email>
		<Customer_Phone>(718) 662-6105</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-9</last_update>
	</record>
	<record>
		<Customer_PK>476</Customer_PK>
		<Customer_ID>348</Customer_ID>
		<Customer_Name>Neville Vasquez</Customer_Name>
		<Customer_Email>lobortis.quis@aol.com</Customer_Email>
		<Customer_Phone>1-677-627-2414</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-24</last_update>
	</record>
	<record>
		<Customer_PK>477</Customer_PK>
		<Customer_ID>287</Customer_ID>
		<Customer_Name>Bert Hendrix</Customer_Name>
		<Customer_Email>eget.nisi@icloud.ca</Customer_Email>
		<Customer_Phone>(253) 872-8293</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-8</last_update>
	</record>
	<record>
		<Customer_PK>478</Customer_PK>
		<Customer_ID>27</Customer_ID>
		<Customer_Name>Aline Lopez</Customer_Name>
		<Customer_Email>tristique.ac@hotmail.net</Customer_Email>
		<Customer_Phone>(564) 362-4633</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-12</last_update>
	</record>
	<record>
		<Customer_PK>479</Customer_PK>
		<Customer_ID>20</Customer_ID>
		<Customer_Name>Tanya Spence</Customer_Name>
		<Customer_Email>metus.urna@yahoo.ca</Customer_Email>
		<Customer_Phone>(115) 972-8297</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-9-2</last_update>
	</record>
	<record>
		<Customer_PK>480</Customer_PK>
		<Customer_ID>267</Customer_ID>
		<Customer_Name>Lee Bernard</Customer_Name>
		<Customer_Email>cursus.integer@aol.edu</Customer_Email>
		<Customer_Phone>1-663-474-1108</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-20</last_update>
	</record>
	<record>
		<Customer_PK>481</Customer_PK>
		<Customer_ID>49</Customer_ID>
		<Customer_Name>Austin Thompson</Customer_Name>
		<Customer_Email>sed.dictum@icloud.org</Customer_Email>
		<Customer_Phone>1-876-874-7711</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-28</last_update>
	</record>
	<record>
		<Customer_PK>482</Customer_PK>
		<Customer_ID>463</Customer_ID>
		<Customer_Name>Kennan Duke</Customer_Name>
		<Customer_Email>neque.et.nunc@yahoo.edu</Customer_Email>
		<Customer_Phone>(121) 353-3563</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-29</last_update>
	</record>
	<record>
		<Customer_PK>483</Customer_PK>
		<Customer_ID>269</Customer_ID>
		<Customer_Name>Sean Wilcox</Customer_Name>
		<Customer_Email>dui.lectus@aol.couk</Customer_Email>
		<Customer_Phone>1-607-686-5136</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-1</last_update>
	</record>
	<record>
		<Customer_PK>484</Customer_PK>
		<Customer_ID>268</Customer_ID>
		<Customer_Name>Ignatius Vang</Customer_Name>
		<Customer_Email>lorem.eu@aol.edu</Customer_Email>
		<Customer_Phone>1-675-821-3938</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-5-15</last_update>
	</record>
	<record>
		<Customer_PK>485</Customer_PK>
		<Customer_ID>38</Customer_ID>
		<Customer_Name>Forrest Maldonado</Customer_Name>
		<Customer_Email>enim.commodo.hendrerit@protonmail.org</Customer_Email>
		<Customer_Phone>1-477-908-2458</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-4-27</last_update>
	</record>
	<record>
		<Customer_PK>486</Customer_PK>
		<Customer_ID>402</Customer_ID>
		<Customer_Name>Maia Burnett</Customer_Name>
		<Customer_Email>montes.nascetur@protonmail.couk</Customer_Email>
		<Customer_Phone>(615) 251-7780</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-28</last_update>
	</record>
	<record>
		<Customer_PK>487</Customer_PK>
		<Customer_ID>287</Customer_ID>
		<Customer_Name>Fallon Nieves</Customer_Name>
		<Customer_Email>purus@aol.ca</Customer_Email>
		<Customer_Phone>(448) 856-0373</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-15</last_update>
	</record>
	<record>
		<Customer_PK>488</Customer_PK>
		<Customer_ID>285</Customer_ID>
		<Customer_Name>Veda Craft</Customer_Name>
		<Customer_Email>dui.cras@icloud.edu</Customer_Email>
		<Customer_Phone>1-522-681-7314</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-10</last_update>
	</record>
	<record>
		<Customer_PK>489</Customer_PK>
		<Customer_ID>149</Customer_ID>
		<Customer_Name>Quentin Huffman</Customer_Name>
		<Customer_Email>auctor.mauris.vel@aol.net</Customer_Email>
		<Customer_Phone>1-711-579-2719</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-10</last_update>
	</record>
	<record>
		<Customer_PK>490</Customer_PK>
		<Customer_ID>467</Customer_ID>
		<Customer_Name>Yuli Clay</Customer_Name>
		<Customer_Email>elit@google.org</Customer_Email>
		<Customer_Phone>1-138-218-5374</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-1-7</last_update>
	</record>
	<record>
		<Customer_PK>491</Customer_PK>
		<Customer_ID>141</Customer_ID>
		<Customer_Name>Amber Browning</Customer_Name>
		<Customer_Email>adipiscing.lacus@outlook.org</Customer_Email>
		<Customer_Phone>1-531-489-9356</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-11-15</last_update>
	</record>
	<record>
		<Customer_PK>492</Customer_PK>
		<Customer_ID>460</Customer_ID>
		<Customer_Name>Bertha Bolton</Customer_Name>
		<Customer_Email>est.tempor@hotmail.edu</Customer_Email>
		<Customer_Phone>(535) 919-0829</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-7</last_update>
	</record>
	<record>
		<Customer_PK>493</Customer_PK>
		<Customer_ID>165</Customer_ID>
		<Customer_Name>Allistair Ford</Customer_Name>
		<Customer_Email>gravida.aliquam@protonmail.net</Customer_Email>
		<Customer_Phone>1-246-445-8155</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-2</last_update>
	</record>
	<record>
		<Customer_PK>494</Customer_PK>
		<Customer_ID>285</Customer_ID>
		<Customer_Name>Melanie Owen</Customer_Name>
		<Customer_Email>nisl.nulla@hotmail.couk</Customer_Email>
		<Customer_Phone>1-784-870-6311</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-5-6</last_update>
	</record>
	<record>
		<Customer_PK>495</Customer_PK>
		<Customer_ID>69</Customer_ID>
		<Customer_Name>Eve Slater</Customer_Name>
		<Customer_Email>sed.leo@icloud.ca</Customer_Email>
		<Customer_Phone>(369) 904-8213</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-6</last_update>
	</record>
	<record>
		<Customer_PK>496</Customer_PK>
		<Customer_ID>258</Customer_ID>
		<Customer_Name>Amal Joseph</Customer_Name>
		<Customer_Email>mauris.rhoncus@icloud.org</Customer_Email>
		<Customer_Phone>(311) 545-5251</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-8</last_update>
	</record>
	<record>
		<Customer_PK>497</Customer_PK>
		<Customer_ID>60</Customer_ID>
		<Customer_Name>Helen Guy</Customer_Name>
		<Customer_Email>duis.elementum.dui@outlook.ca</Customer_Email>
		<Customer_Phone>1-446-412-3353</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-18</last_update>
	</record>
	<record>
		<Customer_PK>498</Customer_PK>
		<Customer_ID>362</Customer_ID>
		<Customer_Name>Oliver Mccall</Customer_Name>
		<Customer_Email>neque.in.ornare@outlook.net</Customer_Email>
		<Customer_Phone>1-539-421-7615</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-16</last_update>
	</record>
	<record>
		<Customer_PK>499</Customer_PK>
		<Customer_ID>49</Customer_ID>
		<Customer_Name>Piper Koch</Customer_Name>
		<Customer_Email>enim.gravida.sit@yahoo.org</Customer_Email>
		<Customer_Phone>(207) 480-6385</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-29</last_update>
	</record>
	<record>
		<Customer_PK>500</Customer_PK>
		<Customer_ID>238</Customer_ID>
		<Customer_Name>Giacomo Aguilar</Customer_Name>
		<Customer_Email>lorem.fringilla@aol.edu</Customer_Email>
		<Customer_Phone>1-456-258-4443</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-9-15</last_update>
	</record>
	<record>
		<Customer_PK>501</Customer_PK>
		<Customer_ID>936</Customer_ID>
		<Customer_Name>TaShya Fitzgerald</Customer_Name>
		<Customer_Email>mollis.duis@icloud.com</Customer_Email>
		<Customer_Phone>1-680-437-5542</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-9-25</last_update>
	</record>
	<record>
		<Customer_PK>502</Customer_PK>
		<Customer_ID>746</Customer_ID>
		<Customer_Name>Rinah Cooper</Customer_Name>
		<Customer_Email>eu@aol.edu</Customer_Email>
		<Customer_Phone>1-356-628-3463</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-22</last_update>
	</record>
	<record>
		<Customer_PK>503</Customer_PK>
		<Customer_ID>630</Customer_ID>
		<Customer_Name>Tyler Cummings</Customer_Name>
		<Customer_Email>id.blandit@outlook.edu</Customer_Email>
		<Customer_Phone>(466) 787-2269</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-5</last_update>
	</record>
	<record>
		<Customer_PK>504</Customer_PK>
		<Customer_ID>855</Customer_ID>
		<Customer_Name>Erica Patton</Customer_Name>
		<Customer_Email>iaculis.enim.sit@yahoo.ca</Customer_Email>
		<Customer_Phone>1-632-332-6684</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-4</last_update>
	</record>
	<record>
		<Customer_PK>505</Customer_PK>
		<Customer_ID>879</Customer_ID>
		<Customer_Name>Plato Spears</Customer_Name>
		<Customer_Email>suscipit.est@icloud.edu</Customer_Email>
		<Customer_Phone>(513) 657-4138</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-23</last_update>
	</record>
	<record>
		<Customer_PK>506</Customer_PK>
		<Customer_ID>511</Customer_ID>
		<Customer_Name>Aristotle Rivers</Customer_Name>
		<Customer_Email>arcu.eu@google.com</Customer_Email>
		<Customer_Phone>1-133-333-5169</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-12</last_update>
	</record>
	<record>
		<Customer_PK>507</Customer_PK>
		<Customer_ID>695</Customer_ID>
		<Customer_Name>Kiona Clayton</Customer_Name>
		<Customer_Email>mauris@hotmail.org</Customer_Email>
		<Customer_Phone>1-257-871-2682</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-4</last_update>
	</record>
	<record>
		<Customer_PK>508</Customer_PK>
		<Customer_ID>864</Customer_ID>
		<Customer_Name>Yael Chambers</Customer_Name>
		<Customer_Email>ornare@hotmail.com</Customer_Email>
		<Customer_Phone>1-317-835-8555</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-9-14</last_update>
	</record>
	<record>
		<Customer_PK>509</Customer_PK>
		<Customer_ID>1000</Customer_ID>
		<Customer_Name>Regan Fox</Customer_Name>
		<Customer_Email>etiam.vestibulum@aol.net</Customer_Email>
		<Customer_Phone>(691) 566-3552</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-9-4</last_update>
	</record>
	<record>
		<Customer_PK>510</Customer_PK>
		<Customer_ID>602</Customer_ID>
		<Customer_Name>Martina Rich</Customer_Name>
		<Customer_Email>ipsum.non@icloud.ca</Customer_Email>
		<Customer_Phone>(157) 763-2073</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-11-2</last_update>
	</record>
	<record>
		<Customer_PK>511</Customer_PK>
		<Customer_ID>910</Customer_ID>
		<Customer_Name>Gail Casey</Customer_Name>
		<Customer_Email>non.cursus@icloud.com</Customer_Email>
		<Customer_Phone>1-866-475-6128</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-4-26</last_update>
	</record>
	<record>
		<Customer_PK>512</Customer_PK>
		<Customer_ID>735</Customer_ID>
		<Customer_Name>Hamilton Riley</Customer_Name>
		<Customer_Email>purus.sapien@protonmail.ca</Customer_Email>
		<Customer_Phone>(535) 272-0255</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-9-9</last_update>
	</record>
	<record>
		<Customer_PK>513</Customer_PK>
		<Customer_ID>574</Customer_ID>
		<Customer_Name>Lacey Combs</Customer_Name>
		<Customer_Email>quisque@google.ca</Customer_Email>
		<Customer_Phone>(846) 651-0401</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-15</last_update>
	</record>
	<record>
		<Customer_PK>514</Customer_PK>
		<Customer_ID>564</Customer_ID>
		<Customer_Name>Zahir Villarreal</Customer_Name>
		<Customer_Email>ante@google.com</Customer_Email>
		<Customer_Phone>1-917-797-6192</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-9-1</last_update>
	</record>
	<record>
		<Customer_PK>515</Customer_PK>
		<Customer_ID>818</Customer_ID>
		<Customer_Name>Allistair Kline</Customer_Name>
		<Customer_Email>accumsan.convallis@google.com</Customer_Email>
		<Customer_Phone>1-998-134-5259</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-5-17</last_update>
	</record>
	<record>
		<Customer_PK>516</Customer_PK>
		<Customer_ID>892</Customer_ID>
		<Customer_Name>Mara Patton</Customer_Name>
		<Customer_Email>magna.sed.dui@protonmail.couk</Customer_Email>
		<Customer_Phone>1-827-619-3322</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-5</last_update>
	</record>
	<record>
		<Customer_PK>517</Customer_PK>
		<Customer_ID>584</Customer_ID>
		<Customer_Name>Adrienne Huffman</Customer_Name>
		<Customer_Email>scelerisque.scelerisque@protonmail.net</Customer_Email>
		<Customer_Phone>1-262-605-4290</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-5-22</last_update>
	</record>
	<record>
		<Customer_PK>518</Customer_PK>
		<Customer_ID>662</Customer_ID>
		<Customer_Name>Igor Valenzuela</Customer_Name>
		<Customer_Email>praesent.eu.dui@aol.org</Customer_Email>
		<Customer_Phone>1-443-446-5105</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-2-21</last_update>
	</record>
	<record>
		<Customer_PK>519</Customer_PK>
		<Customer_ID>711</Customer_ID>
		<Customer_Name>Donovan Swanson</Customer_Name>
		<Customer_Email>porttitor@outlook.ca</Customer_Email>
		<Customer_Phone>1-834-107-5983</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-8-8</last_update>
	</record>
	<record>
		<Customer_PK>520</Customer_PK>
		<Customer_ID>611</Customer_ID>
		<Customer_Name>Tanner Brewer</Customer_Name>
		<Customer_Email>eget.ipsum.donec@icloud.edu</Customer_Email>
		<Customer_Phone>1-567-863-4667</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-2-5</last_update>
	</record>
	<record>
		<Customer_PK>521</Customer_PK>
		<Customer_ID>994</Customer_ID>
		<Customer_Name>Thane Snider</Customer_Name>
		<Customer_Email>a.dui@protonmail.edu</Customer_Email>
		<Customer_Phone>1-843-535-5588</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-4</last_update>
	</record>
	<record>
		<Customer_PK>522</Customer_PK>
		<Customer_ID>505</Customer_ID>
		<Customer_Name>Rafael Riddle</Customer_Name>
		<Customer_Email>magna.sed.dui@hotmail.org</Customer_Email>
		<Customer_Phone>(282) 884-2012</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-29</last_update>
	</record>
	<record>
		<Customer_PK>523</Customer_PK>
		<Customer_ID>547</Customer_ID>
		<Customer_Name>Lareina Zimmerman</Customer_Name>
		<Customer_Email>eu.augue@outlook.ca</Customer_Email>
		<Customer_Phone>1-313-437-0281</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-5</last_update>
	</record>
	<record>
		<Customer_PK>524</Customer_PK>
		<Customer_ID>579</Customer_ID>
		<Customer_Name>Dorothy Reynolds</Customer_Name>
		<Customer_Email>ornare.elit@protonmail.com</Customer_Email>
		<Customer_Phone>1-464-318-4186</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-14</last_update>
	</record>
	<record>
		<Customer_PK>525</Customer_PK>
		<Customer_ID>883</Customer_ID>
		<Customer_Name>Martha Chavez</Customer_Name>
		<Customer_Email>interdum.feugiat@hotmail.com</Customer_Email>
		<Customer_Phone>1-754-410-8308</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-9-5</last_update>
	</record>
	<record>
		<Customer_PK>526</Customer_PK>
		<Customer_ID>579</Customer_ID>
		<Customer_Name>Ainsley Bean</Customer_Name>
		<Customer_Email>dolor.dapibus@icloud.edu</Customer_Email>
		<Customer_Phone>1-115-921-3942</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-24</last_update>
	</record>
	<record>
		<Customer_PK>527</Customer_PK>
		<Customer_ID>702</Customer_ID>
		<Customer_Name>Aimee Head</Customer_Name>
		<Customer_Email>sem.mollis.dui@aol.net</Customer_Email>
		<Customer_Phone>1-565-637-5537</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-4</last_update>
	</record>
	<record>
		<Customer_PK>528</Customer_PK>
		<Customer_ID>515</Customer_ID>
		<Customer_Name>Brielle Nicholson</Customer_Name>
		<Customer_Email>non@google.net</Customer_Email>
		<Customer_Phone>1-228-467-2253</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-11-14</last_update>
	</record>
	<record>
		<Customer_PK>529</Customer_PK>
		<Customer_ID>830</Customer_ID>
		<Customer_Name>Baker Ray</Customer_Name>
		<Customer_Email>eu.metus@icloud.edu</Customer_Email>
		<Customer_Phone>1-181-756-4138</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-23</last_update>
	</record>
	<record>
		<Customer_PK>530</Customer_PK>
		<Customer_ID>584</Customer_ID>
		<Customer_Name>Wang Gardner</Customer_Name>
		<Customer_Email>nunc.risus.varius@hotmail.com</Customer_Email>
		<Customer_Phone>1-844-405-5680</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-2</last_update>
	</record>
	<record>
		<Customer_PK>531</Customer_PK>
		<Customer_ID>777</Customer_ID>
		<Customer_Name>Jaime King</Customer_Name>
		<Customer_Email>nunc@yahoo.couk</Customer_Email>
		<Customer_Phone>(349) 569-5827</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-27</last_update>
	</record>
	<record>
		<Customer_PK>532</Customer_PK>
		<Customer_ID>694</Customer_ID>
		<Customer_Name>Mannix Aguirre</Customer_Name>
		<Customer_Email>a.magna@protonmail.org</Customer_Email>
		<Customer_Phone>(848) 256-4815</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-3</last_update>
	</record>
	<record>
		<Customer_PK>533</Customer_PK>
		<Customer_ID>691</Customer_ID>
		<Customer_Name>Cedric Goodwin</Customer_Name>
		<Customer_Email>id.enim@yahoo.ca</Customer_Email>
		<Customer_Phone>(787) 824-7755</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-10</last_update>
	</record>
	<record>
		<Customer_PK>534</Customer_PK>
		<Customer_ID>852</Customer_ID>
		<Customer_Name>Baker Stafford</Customer_Name>
		<Customer_Email>donec.non@outlook.edu</Customer_Email>
		<Customer_Phone>(482) 701-2398</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-16</last_update>
	</record>
	<record>
		<Customer_PK>535</Customer_PK>
		<Customer_ID>717</Customer_ID>
		<Customer_Name>Felix Hudson</Customer_Name>
		<Customer_Email>amet.massa@hotmail.com</Customer_Email>
		<Customer_Phone>1-969-725-4523</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-25</last_update>
	</record>
	<record>
		<Customer_PK>536</Customer_PK>
		<Customer_ID>900</Customer_ID>
		<Customer_Name>Garth Figueroa</Customer_Name>
		<Customer_Email>velit.eget.laoreet@hotmail.com</Customer_Email>
		<Customer_Phone>1-627-134-7315</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-1</last_update>
	</record>
	<record>
		<Customer_PK>537</Customer_PK>
		<Customer_ID>930</Customer_ID>
		<Customer_Name>Hamish Morales</Customer_Name>
		<Customer_Email>magna.phasellus@google.couk</Customer_Email>
		<Customer_Phone>(931) 597-1261</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-28</last_update>
	</record>
	<record>
		<Customer_PK>538</Customer_PK>
		<Customer_ID>778</Customer_ID>
		<Customer_Name>Eliana Mcdowell</Customer_Name>
		<Customer_Email>cursus.purus@outlook.org</Customer_Email>
		<Customer_Phone>(863) 573-3423</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-5-1</last_update>
	</record>
	<record>
		<Customer_PK>539</Customer_PK>
		<Customer_ID>641</Customer_ID>
		<Customer_Name>MacKensie Cardenas</Customer_Name>
		<Customer_Email>eget.venenatis.a@yahoo.edu</Customer_Email>
		<Customer_Phone>1-621-835-0466</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-4-16</last_update>
	</record>
	<record>
		<Customer_PK>540</Customer_PK>
		<Customer_ID>619</Customer_ID>
		<Customer_Name>Erasmus Wilson</Customer_Name>
		<Customer_Email>molestie.tellus@icloud.org</Customer_Email>
		<Customer_Phone>1-433-215-1326</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-22</last_update>
	</record>
	<record>
		<Customer_PK>541</Customer_PK>
		<Customer_ID>855</Customer_ID>
		<Customer_Name>Daniel Lang</Customer_Name>
		<Customer_Email>et@protonmail.net</Customer_Email>
		<Customer_Phone>1-492-181-4565</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-11-3</last_update>
	</record>
	<record>
		<Customer_PK>542</Customer_PK>
		<Customer_ID>606</Customer_ID>
		<Customer_Name>Thor Willis</Customer_Name>
		<Customer_Email>in@icloud.edu</Customer_Email>
		<Customer_Phone>(792) 125-1698</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-9</last_update>
	</record>
	<record>
		<Customer_PK>543</Customer_PK>
		<Customer_ID>638</Customer_ID>
		<Customer_Name>Richard Landry</Customer_Name>
		<Customer_Email>augue.scelerisque@aol.net</Customer_Email>
		<Customer_Phone>1-125-821-2554</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-3</last_update>
	</record>
	<record>
		<Customer_PK>544</Customer_PK>
		<Customer_ID>896</Customer_ID>
		<Customer_Name>David Wolfe</Customer_Name>
		<Customer_Email>tortor.integer.aliquam@protonmail.couk</Customer_Email>
		<Customer_Phone>1-325-945-2607</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-18</last_update>
	</record>
	<record>
		<Customer_PK>545</Customer_PK>
		<Customer_ID>704</Customer_ID>
		<Customer_Name>Keiko Emerson</Customer_Name>
		<Customer_Email>sed.pharetra@aol.couk</Customer_Email>
		<Customer_Phone>(231) 254-3737</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-30</last_update>
	</record>
	<record>
		<Customer_PK>546</Customer_PK>
		<Customer_ID>604</Customer_ID>
		<Customer_Name>Lester Giles</Customer_Name>
		<Customer_Email>arcu.curabitur@protonmail.com</Customer_Email>
		<Customer_Phone>(390) 663-6493</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-29</last_update>
	</record>
	<record>
		<Customer_PK>547</Customer_PK>
		<Customer_ID>906</Customer_ID>
		<Customer_Name>Pascale Reyes</Customer_Name>
		<Customer_Email>sapien.nunc.pulvinar@hotmail.org</Customer_Email>
		<Customer_Phone>(680) 486-5006</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-14</last_update>
	</record>
	<record>
		<Customer_PK>548</Customer_PK>
		<Customer_ID>669</Customer_ID>
		<Customer_Name>Sharon Alford</Customer_Name>
		<Customer_Email>mi@icloud.net</Customer_Email>
		<Customer_Phone>(769) 827-1355</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-5-6</last_update>
	</record>
	<record>
		<Customer_PK>549</Customer_PK>
		<Customer_ID>880</Customer_ID>
		<Customer_Name>Rafael Morton</Customer_Name>
		<Customer_Email>ligula@google.couk</Customer_Email>
		<Customer_Phone>(265) 854-1223</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-8-7</last_update>
	</record>
	<record>
		<Customer_PK>550</Customer_PK>
		<Customer_ID>534</Customer_ID>
		<Customer_Name>Amaya Hodge</Customer_Name>
		<Customer_Email>fusce.aliquam.enim@icloud.couk</Customer_Email>
		<Customer_Phone>1-371-204-3153</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-20</last_update>
	</record>
	<record>
		<Customer_PK>551</Customer_PK>
		<Customer_ID>813</Customer_ID>
		<Customer_Name>Keiko Steele</Customer_Name>
		<Customer_Email>in.dolor@outlook.com</Customer_Email>
		<Customer_Phone>(717) 406-5977</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-22</last_update>
	</record>
	<record>
		<Customer_PK>552</Customer_PK>
		<Customer_ID>887</Customer_ID>
		<Customer_Name>Marsden Hickman</Customer_Name>
		<Customer_Email>sagittis.semper@hotmail.couk</Customer_Email>
		<Customer_Phone>(643) 713-2506</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-28</last_update>
	</record>
	<record>
		<Customer_PK>553</Customer_PK>
		<Customer_ID>675</Customer_ID>
		<Customer_Name>Josephine Preston</Customer_Name>
		<Customer_Email>egestas@hotmail.ca</Customer_Email>
		<Customer_Phone>(751) 754-6528</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-15</last_update>
	</record>
	<record>
		<Customer_PK>554</Customer_PK>
		<Customer_ID>623</Customer_ID>
		<Customer_Name>Sage Dyer</Customer_Name>
		<Customer_Email>integer@google.com</Customer_Email>
		<Customer_Phone>(398) 423-4326</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-9-18</last_update>
	</record>
	<record>
		<Customer_PK>555</Customer_PK>
		<Customer_ID>938</Customer_ID>
		<Customer_Name>Ira Reynolds</Customer_Name>
		<Customer_Email>hendrerit@outlook.couk</Customer_Email>
		<Customer_Phone>(493) 668-9885</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-5</last_update>
	</record>
	<record>
		<Customer_PK>556</Customer_PK>
		<Customer_ID>673</Customer_ID>
		<Customer_Name>Dolan Thornton</Customer_Name>
		<Customer_Email>tellus@aol.com</Customer_Email>
		<Customer_Phone>1-536-107-2847</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-14</last_update>
	</record>
	<record>
		<Customer_PK>557</Customer_PK>
		<Customer_ID>750</Customer_ID>
		<Customer_Name>Tara Jones</Customer_Name>
		<Customer_Email>auctor.quis@icloud.couk</Customer_Email>
		<Customer_Phone>(837) 982-9781</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-25</last_update>
	</record>
	<record>
		<Customer_PK>558</Customer_PK>
		<Customer_ID>577</Customer_ID>
		<Customer_Name>Drake Kane</Customer_Name>
		<Customer_Email>risus.quis.diam@hotmail.ca</Customer_Email>
		<Customer_Phone>1-933-777-3345</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-4</last_update>
	</record>
	<record>
		<Customer_PK>559</Customer_PK>
		<Customer_ID>615</Customer_ID>
		<Customer_Name>Freya Oneal</Customer_Name>
		<Customer_Email>id@outlook.edu</Customer_Email>
		<Customer_Phone>1-623-574-9519</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-17</last_update>
	</record>
	<record>
		<Customer_PK>560</Customer_PK>
		<Customer_ID>508</Customer_ID>
		<Customer_Name>Caesar Knapp</Customer_Name>
		<Customer_Email>dolor@aol.net</Customer_Email>
		<Customer_Phone>(406) 963-4746</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-11</last_update>
	</record>
	<record>
		<Customer_PK>561</Customer_PK>
		<Customer_ID>836</Customer_ID>
		<Customer_Name>Cleo Mercer</Customer_Name>
		<Customer_Email>tellus@google.net</Customer_Email>
		<Customer_Phone>1-557-466-3444</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-15</last_update>
	</record>
	<record>
		<Customer_PK>562</Customer_PK>
		<Customer_ID>504</Customer_ID>
		<Customer_Name>Acton Evans</Customer_Name>
		<Customer_Email>elit@hotmail.net</Customer_Email>
		<Customer_Phone>1-261-922-2421</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-11-30</last_update>
	</record>
	<record>
		<Customer_PK>563</Customer_PK>
		<Customer_ID>672</Customer_ID>
		<Customer_Name>Alexa Rivas</Customer_Name>
		<Customer_Email>sem.elit@aol.com</Customer_Email>
		<Customer_Phone>1-720-543-8388</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-22</last_update>
	</record>
	<record>
		<Customer_PK>564</Customer_PK>
		<Customer_ID>777</Customer_ID>
		<Customer_Name>Russell Davenport</Customer_Name>
		<Customer_Email>facilisis.non@protonmail.ca</Customer_Email>
		<Customer_Phone>(629) 414-0621</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-8</last_update>
	</record>
	<record>
		<Customer_PK>565</Customer_PK>
		<Customer_ID>674</Customer_ID>
		<Customer_Name>Vladimir Kinney</Customer_Name>
		<Customer_Email>cras.eget@icloud.com</Customer_Email>
		<Customer_Phone>1-251-228-4584</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-3</last_update>
	</record>
	<record>
		<Customer_PK>566</Customer_PK>
		<Customer_ID>735</Customer_ID>
		<Customer_Name>Wade Navarro</Customer_Name>
		<Customer_Email>semper@hotmail.ca</Customer_Email>
		<Customer_Phone>1-616-149-6828</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-12</last_update>
	</record>
	<record>
		<Customer_PK>567</Customer_PK>
		<Customer_ID>603</Customer_ID>
		<Customer_Name>Leroy Marsh</Customer_Name>
		<Customer_Email>dignissim.tempor@protonmail.org</Customer_Email>
		<Customer_Phone>1-550-382-5365</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-31</last_update>
	</record>
	<record>
		<Customer_PK>568</Customer_PK>
		<Customer_ID>970</Customer_ID>
		<Customer_Name>Samson Fowler</Customer_Name>
		<Customer_Email>vehicula.aliquet@google.org</Customer_Email>
		<Customer_Phone>(384) 320-3932</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-2</last_update>
	</record>
	<record>
		<Customer_PK>569</Customer_PK>
		<Customer_ID>980</Customer_ID>
		<Customer_Name>Brent Bright</Customer_Name>
		<Customer_Email>ac.orci@aol.net</Customer_Email>
		<Customer_Phone>(242) 706-4865</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-28</last_update>
	</record>
	<record>
		<Customer_PK>570</Customer_PK>
		<Customer_ID>621</Customer_ID>
		<Customer_Name>Clare Cherry</Customer_Name>
		<Customer_Email>duis@outlook.edu</Customer_Email>
		<Customer_Phone>1-583-856-4812</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-30</last_update>
	</record>
	<record>
		<Customer_PK>571</Customer_PK>
		<Customer_ID>860</Customer_ID>
		<Customer_Name>Danielle Wong</Customer_Name>
		<Customer_Email>justo.sit@outlook.edu</Customer_Email>
		<Customer_Phone>(972) 862-8400</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-17</last_update>
	</record>
	<record>
		<Customer_PK>572</Customer_PK>
		<Customer_ID>551</Customer_ID>
		<Customer_Name>Nola Francis</Customer_Name>
		<Customer_Email>nunc.mauris.morbi@hotmail.edu</Customer_Email>
		<Customer_Phone>1-874-149-2067</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-6</last_update>
	</record>
	<record>
		<Customer_PK>573</Customer_PK>
		<Customer_ID>516</Customer_ID>
		<Customer_Name>Chase Blackwell</Customer_Name>
		<Customer_Email>nec.tempus.scelerisque@google.ca</Customer_Email>
		<Customer_Phone>1-332-766-6987</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-30</last_update>
	</record>
	<record>
		<Customer_PK>574</Customer_PK>
		<Customer_ID>627</Customer_ID>
		<Customer_Name>Vivian Boyer</Customer_Name>
		<Customer_Email>faucibus@aol.net</Customer_Email>
		<Customer_Phone>1-862-394-7623</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-19</last_update>
	</record>
	<record>
		<Customer_PK>575</Customer_PK>
		<Customer_ID>722</Customer_ID>
		<Customer_Name>Maya Morse</Customer_Name>
		<Customer_Email>nullam.velit@aol.org</Customer_Email>
		<Customer_Phone>(243) 188-7438</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-4</last_update>
	</record>
	<record>
		<Customer_PK>576</Customer_PK>
		<Customer_ID>641</Customer_ID>
		<Customer_Name>Daphne Winters</Customer_Name>
		<Customer_Email>metus@protonmail.edu</Customer_Email>
		<Customer_Phone>1-929-618-1654</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-8</last_update>
	</record>
	<record>
		<Customer_PK>577</Customer_PK>
		<Customer_ID>656</Customer_ID>
		<Customer_Name>Grace Koch</Customer_Name>
		<Customer_Email>augue@aol.com</Customer_Email>
		<Customer_Phone>1-689-614-5447</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-8</last_update>
	</record>
	<record>
		<Customer_PK>578</Customer_PK>
		<Customer_ID>674</Customer_ID>
		<Customer_Name>Germaine Cantrell</Customer_Name>
		<Customer_Email>a.enim@icloud.ca</Customer_Email>
		<Customer_Phone>(441) 973-3263</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-29</last_update>
	</record>
	<record>
		<Customer_PK>579</Customer_PK>
		<Customer_ID>686</Customer_ID>
		<Customer_Name>Jonas Bradford</Customer_Name>
		<Customer_Email>ut@aol.couk</Customer_Email>
		<Customer_Phone>(511) 486-5437</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-25</last_update>
	</record>
	<record>
		<Customer_PK>580</Customer_PK>
		<Customer_ID>967</Customer_ID>
		<Customer_Name>Eaton Britt</Customer_Name>
		<Customer_Email>libero@outlook.com</Customer_Email>
		<Customer_Phone>1-838-659-8882</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-10-19</last_update>
	</record>
	<record>
		<Customer_PK>581</Customer_PK>
		<Customer_ID>702</Customer_ID>
		<Customer_Name>Amethyst Reilly</Customer_Name>
		<Customer_Email>curabitur.dictum@aol.couk</Customer_Email>
		<Customer_Phone>(668) 337-3610</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-30</last_update>
	</record>
	<record>
		<Customer_PK>582</Customer_PK>
		<Customer_ID>535</Customer_ID>
		<Customer_Name>Lunea Pitts</Customer_Name>
		<Customer_Email>diam.at.pretium@yahoo.com</Customer_Email>
		<Customer_Phone>(682) 170-8225</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-14</last_update>
	</record>
	<record>
		<Customer_PK>583</Customer_PK>
		<Customer_ID>584</Customer_ID>
		<Customer_Name>Leilani Fuller</Customer_Name>
		<Customer_Email>nulla.magna@icloud.edu</Customer_Email>
		<Customer_Phone>(122) 807-8632</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-28</last_update>
	</record>
	<record>
		<Customer_PK>584</Customer_PK>
		<Customer_ID>560</Customer_ID>
		<Customer_Name>Dorian Stuart</Customer_Name>
		<Customer_Email>augue.eu@hotmail.ca</Customer_Email>
		<Customer_Phone>(863) 893-5433</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-22</last_update>
	</record>
	<record>
		<Customer_PK>585</Customer_PK>
		<Customer_ID>833</Customer_ID>
		<Customer_Name>Keegan Hatfield</Customer_Name>
		<Customer_Email>purus.nullam@aol.org</Customer_Email>
		<Customer_Phone>1-972-126-7780</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-13</last_update>
	</record>
	<record>
		<Customer_PK>586</Customer_PK>
		<Customer_ID>801</Customer_ID>
		<Customer_Name>Cathleen Reyes</Customer_Name>
		<Customer_Email>ut.pharetra@yahoo.edu</Customer_Email>
		<Customer_Phone>(723) 544-2704</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-2-14</last_update>
	</record>
	<record>
		<Customer_PK>587</Customer_PK>
		<Customer_ID>812</Customer_ID>
		<Customer_Name>Bruce Hull</Customer_Name>
		<Customer_Email>sed.eu.eros@icloud.ca</Customer_Email>
		<Customer_Phone>1-311-743-3217</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-22</last_update>
	</record>
	<record>
		<Customer_PK>588</Customer_PK>
		<Customer_ID>858</Customer_ID>
		<Customer_Name>Colorado Case</Customer_Name>
		<Customer_Email>diam.proin.dolor@icloud.com</Customer_Email>
		<Customer_Phone>(511) 583-1336</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-25</last_update>
	</record>
	<record>
		<Customer_PK>589</Customer_PK>
		<Customer_ID>721</Customer_ID>
		<Customer_Name>Karly Lawson</Customer_Name>
		<Customer_Email>magna.lorem@hotmail.edu</Customer_Email>
		<Customer_Phone>(373) 180-1246</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-27</last_update>
	</record>
	<record>
		<Customer_PK>590</Customer_PK>
		<Customer_ID>559</Customer_ID>
		<Customer_Name>Wing Lamb</Customer_Name>
		<Customer_Email>tristique.pharetra.quisque@protonmail.net</Customer_Email>
		<Customer_Phone>1-867-826-2183</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-22</last_update>
	</record>
	<record>
		<Customer_PK>591</Customer_PK>
		<Customer_ID>891</Customer_ID>
		<Customer_Name>Gail Hampton</Customer_Name>
		<Customer_Email>donec.tempus.lorem@icloud.net</Customer_Email>
		<Customer_Phone>(720) 732-4881</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-10-17</last_update>
	</record>
	<record>
		<Customer_PK>592</Customer_PK>
		<Customer_ID>632</Customer_ID>
		<Customer_Name>Ursa Hyde</Customer_Name>
		<Customer_Email>dapibus.gravida@protonmail.ca</Customer_Email>
		<Customer_Phone>(323) 855-8112</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-20</last_update>
	</record>
	<record>
		<Customer_PK>593</Customer_PK>
		<Customer_ID>942</Customer_ID>
		<Customer_Name>Nora Torres</Customer_Name>
		<Customer_Email>donec@outlook.edu</Customer_Email>
		<Customer_Phone>(281) 521-4224</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-11</last_update>
	</record>
	<record>
		<Customer_PK>594</Customer_PK>
		<Customer_ID>762</Customer_ID>
		<Customer_Name>Sharon Guzman</Customer_Name>
		<Customer_Email>diam.sed@hotmail.org</Customer_Email>
		<Customer_Phone>(231) 945-2847</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-6</last_update>
	</record>
	<record>
		<Customer_PK>595</Customer_PK>
		<Customer_ID>920</Customer_ID>
		<Customer_Name>Sandra Valencia</Customer_Name>
		<Customer_Email>sagittis.augue.eu@yahoo.edu</Customer_Email>
		<Customer_Phone>(333) 472-1370</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-30</last_update>
	</record>
	<record>
		<Customer_PK>596</Customer_PK>
		<Customer_ID>907</Customer_ID>
		<Customer_Name>Unity Vang</Customer_Name>
		<Customer_Email>placerat.augue.sed@google.ca</Customer_Email>
		<Customer_Phone>1-538-471-4297</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-12</last_update>
	</record>
	<record>
		<Customer_PK>597</Customer_PK>
		<Customer_ID>752</Customer_ID>
		<Customer_Name>Ethan Cantu</Customer_Name>
		<Customer_Email>ut.tincidunt.orci@aol.net</Customer_Email>
		<Customer_Phone>1-975-649-3577</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-30</last_update>
	</record>
	<record>
		<Customer_PK>598</Customer_PK>
		<Customer_ID>520</Customer_ID>
		<Customer_Name>Arthur Cain</Customer_Name>
		<Customer_Email>est.mollis.non@outlook.couk</Customer_Email>
		<Customer_Phone>1-100-911-5911</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-20</last_update>
	</record>
	<record>
		<Customer_PK>599</Customer_PK>
		<Customer_ID>735</Customer_ID>
		<Customer_Name>Macaulay Franks</Customer_Name>
		<Customer_Email>est.congue@protonmail.edu</Customer_Email>
		<Customer_Phone>(644) 601-3082</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-5-1</last_update>
	</record>
	<record>
		<Customer_PK>600</Customer_PK>
		<Customer_ID>909</Customer_ID>
		<Customer_Name>Solomon Sampson</Customer_Name>
		<Customer_Email>sed.tortor@protonmail.ca</Customer_Email>
		<Customer_Phone>(561) 668-7541</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-24</last_update>
	</record>
	<record>
		<Customer_PK>601</Customer_PK>
		<Customer_ID>928</Customer_ID>
		<Customer_Name>Gisela Mack</Customer_Name>
		<Customer_Email>eu.accumsan@aol.couk</Customer_Email>
		<Customer_Phone>(187) 606-4871</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-19</last_update>
	</record>
	<record>
		<Customer_PK>602</Customer_PK>
		<Customer_ID>539</Customer_ID>
		<Customer_Name>Reagan Russo</Customer_Name>
		<Customer_Email>phasellus.nulla.integer@icloud.edu</Customer_Email>
		<Customer_Phone>1-286-855-3183</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-12</last_update>
	</record>
	<record>
		<Customer_PK>603</Customer_PK>
		<Customer_ID>847</Customer_ID>
		<Customer_Name>Aladdin Greer</Customer_Name>
		<Customer_Email>mauris@protonmail.couk</Customer_Email>
		<Customer_Phone>1-408-962-3305</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-29</last_update>
	</record>
	<record>
		<Customer_PK>604</Customer_PK>
		<Customer_ID>952</Customer_ID>
		<Customer_Name>Signe Beck</Customer_Name>
		<Customer_Email>mauris.eu.turpis@aol.net</Customer_Email>
		<Customer_Phone>1-969-630-1189</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-9-11</last_update>
	</record>
	<record>
		<Customer_PK>605</Customer_PK>
		<Customer_ID>586</Customer_ID>
		<Customer_Name>Desirae Charles</Customer_Name>
		<Customer_Email>urna.et@protonmail.org</Customer_Email>
		<Customer_Phone>(213) 282-5545</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-11-2</last_update>
	</record>
	<record>
		<Customer_PK>606</Customer_PK>
		<Customer_ID>633</Customer_ID>
		<Customer_Name>Noelle Clark</Customer_Name>
		<Customer_Email>tincidunt.aliquam.arcu@aol.net</Customer_Email>
		<Customer_Phone>(475) 787-4038</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-16</last_update>
	</record>
	<record>
		<Customer_PK>607</Customer_PK>
		<Customer_ID>986</Customer_ID>
		<Customer_Name>Bernard Daugherty</Customer_Name>
		<Customer_Email>ac@yahoo.net</Customer_Email>
		<Customer_Phone>(763) 665-1137</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-2-6</last_update>
	</record>
	<record>
		<Customer_PK>608</Customer_PK>
		<Customer_ID>994</Customer_ID>
		<Customer_Name>Petra Lane</Customer_Name>
		<Customer_Email>vivamus.sit.amet@protonmail.edu</Customer_Email>
		<Customer_Phone>1-665-775-8266</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-13</last_update>
	</record>
	<record>
		<Customer_PK>609</Customer_PK>
		<Customer_ID>602</Customer_ID>
		<Customer_Name>India Morales</Customer_Name>
		<Customer_Email>nullam.nisl.maecenas@protonmail.com</Customer_Email>
		<Customer_Phone>(876) 831-8807</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-29</last_update>
	</record>
	<record>
		<Customer_PK>610</Customer_PK>
		<Customer_ID>954</Customer_ID>
		<Customer_Name>Oprah Tran</Customer_Name>
		<Customer_Email>leo.in.lobortis@hotmail.edu</Customer_Email>
		<Customer_Phone>1-819-268-1045</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-10-12</last_update>
	</record>
	<record>
		<Customer_PK>611</Customer_PK>
		<Customer_ID>501</Customer_ID>
		<Customer_Name>Alan Schwartz</Customer_Name>
		<Customer_Email>mauris.vestibulum.neque@google.com</Customer_Email>
		<Customer_Phone>(291) 771-4407</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-8-23</last_update>
	</record>
	<record>
		<Customer_PK>612</Customer_PK>
		<Customer_ID>861</Customer_ID>
		<Customer_Name>Amena Gordon</Customer_Name>
		<Customer_Email>porttitor.eros.nec@icloud.org</Customer_Email>
		<Customer_Phone>1-469-674-2524</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-26</last_update>
	</record>
	<record>
		<Customer_PK>613</Customer_PK>
		<Customer_ID>700</Customer_ID>
		<Customer_Name>Lester Weiss</Customer_Name>
		<Customer_Email>morbi.sit.amet@icloud.org</Customer_Email>
		<Customer_Phone>1-320-285-7841</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-20</last_update>
	</record>
	<record>
		<Customer_PK>614</Customer_PK>
		<Customer_ID>783</Customer_ID>
		<Customer_Name>Kay Knapp</Customer_Name>
		<Customer_Email>dolor.sit@google.ca</Customer_Email>
		<Customer_Phone>(419) 217-8351</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-4</last_update>
	</record>
	<record>
		<Customer_PK>615</Customer_PK>
		<Customer_ID>991</Customer_ID>
		<Customer_Name>Teegan Scott</Customer_Name>
		<Customer_Email>metus.aliquam.erat@yahoo.org</Customer_Email>
		<Customer_Phone>1-455-245-3511</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-13</last_update>
	</record>
	<record>
		<Customer_PK>616</Customer_PK>
		<Customer_ID>995</Customer_ID>
		<Customer_Name>Burton Kline</Customer_Name>
		<Customer_Email>sed.id.risus@aol.org</Customer_Email>
		<Customer_Phone>1-630-217-5303</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-2</last_update>
	</record>
	<record>
		<Customer_PK>617</Customer_PK>
		<Customer_ID>854</Customer_ID>
		<Customer_Name>Eagan Burke</Customer_Name>
		<Customer_Email>quis@outlook.edu</Customer_Email>
		<Customer_Phone>(490) 427-2222</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-1-19</last_update>
	</record>
	<record>
		<Customer_PK>618</Customer_PK>
		<Customer_ID>754</Customer_ID>
		<Customer_Name>Raja Wooten</Customer_Name>
		<Customer_Email>nam.ac.nulla@yahoo.org</Customer_Email>
		<Customer_Phone>(205) 323-7017</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-12</last_update>
	</record>
	<record>
		<Customer_PK>619</Customer_PK>
		<Customer_ID>869</Customer_ID>
		<Customer_Name>Jocelyn Hayden</Customer_Name>
		<Customer_Email>ac.tellus@outlook.org</Customer_Email>
		<Customer_Phone>(566) 368-9799</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-4-29</last_update>
	</record>
	<record>
		<Customer_PK>620</Customer_PK>
		<Customer_ID>732</Customer_ID>
		<Customer_Name>Daquan Harvey</Customer_Name>
		<Customer_Email>nascetur.ridiculus.mus@google.com</Customer_Email>
		<Customer_Phone>1-555-607-2371</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-11-6</last_update>
	</record>
	<record>
		<Customer_PK>621</Customer_PK>
		<Customer_ID>603</Customer_ID>
		<Customer_Name>Jolie Mcclure</Customer_Name>
		<Customer_Email>bibendum.fermentum.metus@yahoo.couk</Customer_Email>
		<Customer_Phone>(359) 265-3677</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-19</last_update>
	</record>
	<record>
		<Customer_PK>622</Customer_PK>
		<Customer_ID>676</Customer_ID>
		<Customer_Name>Alfonso Cortez</Customer_Name>
		<Customer_Email>lectus.a@hotmail.edu</Customer_Email>
		<Customer_Phone>1-571-740-1236</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-4</last_update>
	</record>
	<record>
		<Customer_PK>623</Customer_PK>
		<Customer_ID>529</Customer_ID>
		<Customer_Name>Aquila Graham</Customer_Name>
		<Customer_Email>nulla@outlook.ca</Customer_Email>
		<Customer_Phone>1-821-924-2583</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-2-27</last_update>
	</record>
	<record>
		<Customer_PK>624</Customer_PK>
		<Customer_ID>924</Customer_ID>
		<Customer_Name>Philip Kramer</Customer_Name>
		<Customer_Email>fermentum.arcu.vestibulum@icloud.net</Customer_Email>
		<Customer_Phone>1-446-312-9356</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-11-3</last_update>
	</record>
	<record>
		<Customer_PK>625</Customer_PK>
		<Customer_ID>858</Customer_ID>
		<Customer_Name>Sheila Reynolds</Customer_Name>
		<Customer_Email>mattis@aol.org</Customer_Email>
		<Customer_Phone>1-486-861-0263</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-1</last_update>
	</record>
	<record>
		<Customer_PK>626</Customer_PK>
		<Customer_ID>930</Customer_ID>
		<Customer_Name>Carl Neal</Customer_Name>
		<Customer_Email>elit.sed@yahoo.net</Customer_Email>
		<Customer_Phone>(435) 321-7767</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-24</last_update>
	</record>
	<record>
		<Customer_PK>627</Customer_PK>
		<Customer_ID>793</Customer_ID>
		<Customer_Name>Pamela Turner</Customer_Name>
		<Customer_Email>ligula.eu@hotmail.couk</Customer_Email>
		<Customer_Phone>1-638-363-1225</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-4-23</last_update>
	</record>
	<record>
		<Customer_PK>628</Customer_PK>
		<Customer_ID>563</Customer_ID>
		<Customer_Name>Moana Ruiz</Customer_Name>
		<Customer_Email>sed@yahoo.org</Customer_Email>
		<Customer_Phone>(212) 818-8413</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-26</last_update>
	</record>
	<record>
		<Customer_PK>629</Customer_PK>
		<Customer_ID>752</Customer_ID>
		<Customer_Name>Camilla Hooper</Customer_Name>
		<Customer_Email>risus.donec@protonmail.ca</Customer_Email>
		<Customer_Phone>1-721-964-3621</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-9-8</last_update>
	</record>
	<record>
		<Customer_PK>630</Customer_PK>
		<Customer_ID>519</Customer_ID>
		<Customer_Name>Urielle Dunn</Customer_Name>
		<Customer_Email>nonummy.ut@icloud.net</Customer_Email>
		<Customer_Phone>(536) 990-0177</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-2</last_update>
	</record>
	<record>
		<Customer_PK>631</Customer_PK>
		<Customer_ID>567</Customer_ID>
		<Customer_Name>Brenna Norman</Customer_Name>
		<Customer_Email>egestas.nunc@icloud.com</Customer_Email>
		<Customer_Phone>1-989-627-7105</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-3</last_update>
	</record>
	<record>
		<Customer_PK>632</Customer_PK>
		<Customer_ID>996</Customer_ID>
		<Customer_Name>Gil Burch</Customer_Name>
		<Customer_Email>mi@hotmail.org</Customer_Email>
		<Customer_Phone>1-834-584-8697</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-10</last_update>
	</record>
	<record>
		<Customer_PK>633</Customer_PK>
		<Customer_ID>979</Customer_ID>
		<Customer_Name>Darrel Marshall</Customer_Name>
		<Customer_Email>enim.consequat@icloud.ca</Customer_Email>
		<Customer_Phone>1-367-435-8821</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-30</last_update>
	</record>
	<record>
		<Customer_PK>634</Customer_PK>
		<Customer_ID>646</Customer_ID>
		<Customer_Name>Glenna Rasmussen</Customer_Name>
		<Customer_Email>justo.nec.ante@google.ca</Customer_Email>
		<Customer_Phone>(211) 246-3462</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-10</last_update>
	</record>
	<record>
		<Customer_PK>635</Customer_PK>
		<Customer_ID>597</Customer_ID>
		<Customer_Name>Marsden Shannon</Customer_Name>
		<Customer_Email>neque@protonmail.edu</Customer_Email>
		<Customer_Phone>(887) 321-6158</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-4</last_update>
	</record>
	<record>
		<Customer_PK>636</Customer_PK>
		<Customer_ID>596</Customer_ID>
		<Customer_Name>Kevyn Gay</Customer_Name>
		<Customer_Email>quisque.ac.libero@outlook.com</Customer_Email>
		<Customer_Phone>(837) 775-7357</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-5-31</last_update>
	</record>
	<record>
		<Customer_PK>637</Customer_PK>
		<Customer_ID>808</Customer_ID>
		<Customer_Name>Danielle Cervantes</Customer_Name>
		<Customer_Email>tincidunt.donec.vitae@protonmail.com</Customer_Email>
		<Customer_Phone>1-643-265-6158</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-1</last_update>
	</record>
	<record>
		<Customer_PK>638</Customer_PK>
		<Customer_ID>927</Customer_ID>
		<Customer_Name>Ava Ramirez</Customer_Name>
		<Customer_Email>adipiscing.non@icloud.com</Customer_Email>
		<Customer_Phone>1-976-301-3328</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-24</last_update>
	</record>
	<record>
		<Customer_PK>639</Customer_PK>
		<Customer_ID>686</Customer_ID>
		<Customer_Name>Joy Pratt</Customer_Name>
		<Customer_Email>in@yahoo.net</Customer_Email>
		<Customer_Phone>1-742-123-3378</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-10-22</last_update>
	</record>
	<record>
		<Customer_PK>640</Customer_PK>
		<Customer_ID>974</Customer_ID>
		<Customer_Name>Gage Lara</Customer_Name>
		<Customer_Email>velit.egestas.lacinia@icloud.edu</Customer_Email>
		<Customer_Phone>(386) 586-8793</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-8-8</last_update>
	</record>
	<record>
		<Customer_PK>641</Customer_PK>
		<Customer_ID>550</Customer_ID>
		<Customer_Name>Richard Greene</Customer_Name>
		<Customer_Email>urna.convallis@yahoo.edu</Customer_Email>
		<Customer_Phone>1-341-721-1838</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-4</last_update>
	</record>
	<record>
		<Customer_PK>642</Customer_PK>
		<Customer_ID>664</Customer_ID>
		<Customer_Name>Chester Harmon</Customer_Name>
		<Customer_Email>risus.quisque@yahoo.com</Customer_Email>
		<Customer_Phone>(920) 617-2448</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-30</last_update>
	</record>
	<record>
		<Customer_PK>643</Customer_PK>
		<Customer_ID>967</Customer_ID>
		<Customer_Name>Marsden Richmond</Customer_Name>
		<Customer_Email>lacus.quisque@aol.couk</Customer_Email>
		<Customer_Phone>1-862-750-2580</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-26</last_update>
	</record>
	<record>
		<Customer_PK>644</Customer_PK>
		<Customer_ID>618</Customer_ID>
		<Customer_Name>Haviva Stevenson</Customer_Name>
		<Customer_Email>suscipit@icloud.net</Customer_Email>
		<Customer_Phone>(610) 430-9491</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-2</last_update>
	</record>
	<record>
		<Customer_PK>645</Customer_PK>
		<Customer_ID>726</Customer_ID>
		<Customer_Name>Adrienne Cash</Customer_Name>
		<Customer_Email>fermentum.metus@protonmail.org</Customer_Email>
		<Customer_Phone>1-861-726-0769</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-4</last_update>
	</record>
	<record>
		<Customer_PK>646</Customer_PK>
		<Customer_ID>849</Customer_ID>
		<Customer_Name>Graham Hurley</Customer_Name>
		<Customer_Email>scelerisque.neque.sed@icloud.couk</Customer_Email>
		<Customer_Phone>1-518-545-5395</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-8-1</last_update>
	</record>
	<record>
		<Customer_PK>647</Customer_PK>
		<Customer_ID>962</Customer_ID>
		<Customer_Name>Chaim Ballard</Customer_Name>
		<Customer_Email>molestie.orci@hotmail.ca</Customer_Email>
		<Customer_Phone>(341) 521-8585</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-26</last_update>
	</record>
	<record>
		<Customer_PK>648</Customer_PK>
		<Customer_ID>780</Customer_ID>
		<Customer_Name>Jescie Fitzpatrick</Customer_Name>
		<Customer_Email>aliquet.vel@outlook.org</Customer_Email>
		<Customer_Phone>(713) 401-9287</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-14</last_update>
	</record>
	<record>
		<Customer_PK>649</Customer_PK>
		<Customer_ID>960</Customer_ID>
		<Customer_Name>Candace Norman</Customer_Name>
		<Customer_Email>cursus.luctus.ipsum@icloud.edu</Customer_Email>
		<Customer_Phone>(553) 664-7561</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-25</last_update>
	</record>
	<record>
		<Customer_PK>650</Customer_PK>
		<Customer_ID>693</Customer_ID>
		<Customer_Name>Signe Gross</Customer_Name>
		<Customer_Email>et.risus.quisque@icloud.net</Customer_Email>
		<Customer_Phone>1-345-170-5319</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-11-29</last_update>
	</record>
	<record>
		<Customer_PK>651</Customer_PK>
		<Customer_ID>667</Customer_ID>
		<Customer_Name>Nita Booker</Customer_Name>
		<Customer_Email>mauris@protonmail.net</Customer_Email>
		<Customer_Phone>(856) 928-5957</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-28</last_update>
	</record>
	<record>
		<Customer_PK>652</Customer_PK>
		<Customer_ID>630</Customer_ID>
		<Customer_Name>Celeste Cooke</Customer_Name>
		<Customer_Email>a.arcu@hotmail.ca</Customer_Email>
		<Customer_Phone>(354) 583-3962</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-3</last_update>
	</record>
	<record>
		<Customer_PK>653</Customer_PK>
		<Customer_ID>724</Customer_ID>
		<Customer_Name>Benjamin Farley</Customer_Name>
		<Customer_Email>lorem@outlook.net</Customer_Email>
		<Customer_Phone>1-478-485-4717</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-19</last_update>
	</record>
	<record>
		<Customer_PK>654</Customer_PK>
		<Customer_ID>719</Customer_ID>
		<Customer_Name>Cara Torres</Customer_Name>
		<Customer_Email>eu.tellus.phasellus@aol.ca</Customer_Email>
		<Customer_Phone>1-756-556-8275</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-9</last_update>
	</record>
	<record>
		<Customer_PK>655</Customer_PK>
		<Customer_ID>970</Customer_ID>
		<Customer_Name>Porter Suarez</Customer_Name>
		<Customer_Email>tempus.eu@protonmail.edu</Customer_Email>
		<Customer_Phone>1-326-966-4539</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-8</last_update>
	</record>
	<record>
		<Customer_PK>656</Customer_PK>
		<Customer_ID>637</Customer_ID>
		<Customer_Name>Barbara O'donnell</Customer_Name>
		<Customer_Email>morbi.vehicula.pellentesque@aol.ca</Customer_Email>
		<Customer_Phone>1-210-298-5574</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-11</last_update>
	</record>
	<record>
		<Customer_PK>657</Customer_PK>
		<Customer_ID>637</Customer_ID>
		<Customer_Name>Kelly Garner</Customer_Name>
		<Customer_Email>mauris.molestie@aol.org</Customer_Email>
		<Customer_Phone>(886) 507-6737</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-7</last_update>
	</record>
	<record>
		<Customer_PK>658</Customer_PK>
		<Customer_ID>701</Customer_ID>
		<Customer_Name>Hakeem Goff</Customer_Name>
		<Customer_Email>interdum.nunc@google.com</Customer_Email>
		<Customer_Phone>1-351-661-3987</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-11-18</last_update>
	</record>
	<record>
		<Customer_PK>659</Customer_PK>
		<Customer_ID>907</Customer_ID>
		<Customer_Name>Brian Ochoa</Customer_Name>
		<Customer_Email>arcu.iaculis@yahoo.net</Customer_Email>
		<Customer_Phone>1-813-390-5195</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-18</last_update>
	</record>
	<record>
		<Customer_PK>660</Customer_PK>
		<Customer_ID>779</Customer_ID>
		<Customer_Name>Nevada Wise</Customer_Name>
		<Customer_Email>et@hotmail.net</Customer_Email>
		<Customer_Phone>1-322-171-5081</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-19</last_update>
	</record>
	<record>
		<Customer_PK>661</Customer_PK>
		<Customer_ID>835</Customer_ID>
		<Customer_Name>Hyatt Duran</Customer_Name>
		<Customer_Email>elit@aol.org</Customer_Email>
		<Customer_Phone>1-536-778-4696</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-14</last_update>
	</record>
	<record>
		<Customer_PK>662</Customer_PK>
		<Customer_ID>675</Customer_ID>
		<Customer_Name>Colette Farrell</Customer_Name>
		<Customer_Email>velit.aliquam@hotmail.couk</Customer_Email>
		<Customer_Phone>1-378-482-5314</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-19</last_update>
	</record>
	<record>
		<Customer_PK>663</Customer_PK>
		<Customer_ID>734</Customer_ID>
		<Customer_Name>Keaton Miranda</Customer_Name>
		<Customer_Email>gravida@protonmail.org</Customer_Email>
		<Customer_Phone>(257) 354-1953</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-8</last_update>
	</record>
	<record>
		<Customer_PK>664</Customer_PK>
		<Customer_ID>956</Customer_ID>
		<Customer_Name>Rose Dejesus</Customer_Name>
		<Customer_Email>magna@outlook.net</Customer_Email>
		<Customer_Phone>1-816-915-2364</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-2-27</last_update>
	</record>
	<record>
		<Customer_PK>665</Customer_PK>
		<Customer_ID>790</Customer_ID>
		<Customer_Name>Stephen Dean</Customer_Name>
		<Customer_Email>dolor.donec.fringilla@hotmail.ca</Customer_Email>
		<Customer_Phone>(381) 512-3830</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-11-1</last_update>
	</record>
	<record>
		<Customer_PK>666</Customer_PK>
		<Customer_ID>665</Customer_ID>
		<Customer_Name>Keefe Haynes</Customer_Name>
		<Customer_Email>nibh.vulputate@outlook.edu</Customer_Email>
		<Customer_Phone>(372) 622-2127</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-16</last_update>
	</record>
	<record>
		<Customer_PK>667</Customer_PK>
		<Customer_ID>933</Customer_ID>
		<Customer_Name>Clio Whitehead</Customer_Name>
		<Customer_Email>convallis.ligula@icloud.ca</Customer_Email>
		<Customer_Phone>(342) 486-9649</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-12</last_update>
	</record>
	<record>
		<Customer_PK>668</Customer_PK>
		<Customer_ID>925</Customer_ID>
		<Customer_Name>Wayne Herring</Customer_Name>
		<Customer_Email>libero@aol.com</Customer_Email>
		<Customer_Phone>1-724-778-7760</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-9</last_update>
	</record>
	<record>
		<Customer_PK>669</Customer_PK>
		<Customer_ID>570</Customer_ID>
		<Customer_Name>Allegra Bishop</Customer_Name>
		<Customer_Email>purus.nullam@aol.ca</Customer_Email>
		<Customer_Phone>(667) 919-4875</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-1-22</last_update>
	</record>
	<record>
		<Customer_PK>670</Customer_PK>
		<Customer_ID>504</Customer_ID>
		<Customer_Name>Caesar Battle</Customer_Name>
		<Customer_Email>at.velit.pellentesque@yahoo.couk</Customer_Email>
		<Customer_Phone>(480) 427-9682</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-8</last_update>
	</record>
	<record>
		<Customer_PK>671</Customer_PK>
		<Customer_ID>752</Customer_ID>
		<Customer_Name>Alexander Franco</Customer_Name>
		<Customer_Email>maecenas@google.com</Customer_Email>
		<Customer_Phone>(833) 453-4566</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-21</last_update>
	</record>
	<record>
		<Customer_PK>672</Customer_PK>
		<Customer_ID>515</Customer_ID>
		<Customer_Name>Sophia Alexander</Customer_Name>
		<Customer_Email>eros@aol.org</Customer_Email>
		<Customer_Phone>(246) 594-5858</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-31</last_update>
	</record>
	<record>
		<Customer_PK>673</Customer_PK>
		<Customer_ID>535</Customer_ID>
		<Customer_Name>Brody Good</Customer_Name>
		<Customer_Email>id.ante@outlook.org</Customer_Email>
		<Customer_Phone>1-116-898-9421</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-12</last_update>
	</record>
	<record>
		<Customer_PK>674</Customer_PK>
		<Customer_ID>626</Customer_ID>
		<Customer_Name>Barclay Garrison</Customer_Name>
		<Customer_Email>tincidunt.orci@yahoo.com</Customer_Email>
		<Customer_Phone>(637) 820-2853</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-2</last_update>
	</record>
	<record>
		<Customer_PK>675</Customer_PK>
		<Customer_ID>669</Customer_ID>
		<Customer_Name>Preston Jenkins</Customer_Name>
		<Customer_Email>ultrices.mauris.ipsum@yahoo.edu</Customer_Email>
		<Customer_Phone>(312) 442-3657</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-31</last_update>
	</record>
	<record>
		<Customer_PK>676</Customer_PK>
		<Customer_ID>526</Customer_ID>
		<Customer_Name>Lucian Reeves</Customer_Name>
		<Customer_Email>convallis.ante.lectus@icloud.edu</Customer_Email>
		<Customer_Phone>(865) 871-3702</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-21</last_update>
	</record>
	<record>
		<Customer_PK>677</Customer_PK>
		<Customer_ID>584</Customer_ID>
		<Customer_Name>Gavin Moses</Customer_Name>
		<Customer_Email>lectus.quis.massa@google.org</Customer_Email>
		<Customer_Phone>1-877-395-5458</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-22</last_update>
	</record>
	<record>
		<Customer_PK>678</Customer_PK>
		<Customer_ID>796</Customer_ID>
		<Customer_Name>Alvin Patton</Customer_Name>
		<Customer_Email>lorem@aol.couk</Customer_Email>
		<Customer_Phone>(551) 413-3769</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-9-2</last_update>
	</record>
	<record>
		<Customer_PK>679</Customer_PK>
		<Customer_ID>884</Customer_ID>
		<Customer_Name>Chaim Dalton</Customer_Name>
		<Customer_Email>integer.tincidunt@google.org</Customer_Email>
		<Customer_Phone>(478) 113-7200</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-25</last_update>
	</record>
	<record>
		<Customer_PK>680</Customer_PK>
		<Customer_ID>844</Customer_ID>
		<Customer_Name>Dorian Greer</Customer_Name>
		<Customer_Email>habitant.morbi.tristique@google.com</Customer_Email>
		<Customer_Phone>1-331-428-6861</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-9</last_update>
	</record>
	<record>
		<Customer_PK>681</Customer_PK>
		<Customer_ID>560</Customer_ID>
		<Customer_Name>Tamara Mccray</Customer_Name>
		<Customer_Email>ultrices.posuere.cubilia@icloud.org</Customer_Email>
		<Customer_Phone>(467) 826-2461</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-2-4</last_update>
	</record>
	<record>
		<Customer_PK>682</Customer_PK>
		<Customer_ID>922</Customer_ID>
		<Customer_Name>Francesca Holmes</Customer_Name>
		<Customer_Email>donec.non@icloud.com</Customer_Email>
		<Customer_Phone>1-746-318-9111</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-16</last_update>
	</record>
	<record>
		<Customer_PK>683</Customer_PK>
		<Customer_ID>657</Customer_ID>
		<Customer_Name>Molly Mendez</Customer_Name>
		<Customer_Email>at@outlook.org</Customer_Email>
		<Customer_Phone>1-230-656-0315</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-8-29</last_update>
	</record>
	<record>
		<Customer_PK>684</Customer_PK>
		<Customer_ID>700</Customer_ID>
		<Customer_Name>Martin Bray</Customer_Name>
		<Customer_Email>amet.ultricies.sem@aol.com</Customer_Email>
		<Customer_Phone>(756) 778-8271</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-21</last_update>
	</record>
	<record>
		<Customer_PK>685</Customer_PK>
		<Customer_ID>804</Customer_ID>
		<Customer_Name>Whilemina Arnold</Customer_Name>
		<Customer_Email>ante.dictum@aol.edu</Customer_Email>
		<Customer_Phone>1-849-478-3424</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-4-21</last_update>
	</record>
	<record>
		<Customer_PK>686</Customer_PK>
		<Customer_ID>601</Customer_ID>
		<Customer_Name>Beck Jacobs</Customer_Name>
		<Customer_Email>quis@google.ca</Customer_Email>
		<Customer_Phone>(623) 788-1276</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-8-15</last_update>
	</record>
	<record>
		<Customer_PK>687</Customer_PK>
		<Customer_ID>941</Customer_ID>
		<Customer_Name>Carol Bray</Customer_Name>
		<Customer_Email>eros.nam@aol.org</Customer_Email>
		<Customer_Phone>(174) 263-1725</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-5</last_update>
	</record>
	<record>
		<Customer_PK>688</Customer_PK>
		<Customer_ID>599</Customer_ID>
		<Customer_Name>Keaton Taylor</Customer_Name>
		<Customer_Email>viverra@yahoo.com</Customer_Email>
		<Customer_Phone>1-685-878-5453</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-28</last_update>
	</record>
	<record>
		<Customer_PK>689</Customer_PK>
		<Customer_ID>923</Customer_ID>
		<Customer_Name>Noelle Ray</Customer_Name>
		<Customer_Email>etiam.gravida@icloud.ca</Customer_Email>
		<Customer_Phone>1-683-843-1767</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-9-28</last_update>
	</record>
	<record>
		<Customer_PK>690</Customer_PK>
		<Customer_ID>948</Customer_ID>
		<Customer_Name>Hasad Guzman</Customer_Name>
		<Customer_Email>mauris.ut@outlook.com</Customer_Email>
		<Customer_Phone>1-257-462-1536</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-18</last_update>
	</record>
	<record>
		<Customer_PK>691</Customer_PK>
		<Customer_ID>987</Customer_ID>
		<Customer_Name>Inez Gates</Customer_Name>
		<Customer_Email>ut.molestie@protonmail.ca</Customer_Email>
		<Customer_Phone>(684) 666-2637</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-20</last_update>
	</record>
	<record>
		<Customer_PK>692</Customer_PK>
		<Customer_ID>551</Customer_ID>
		<Customer_Name>Sara Abbott</Customer_Name>
		<Customer_Email>etiam.laoreet@outlook.couk</Customer_Email>
		<Customer_Phone>(481) 230-7558</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-13</last_update>
	</record>
	<record>
		<Customer_PK>693</Customer_PK>
		<Customer_ID>882</Customer_ID>
		<Customer_Name>Yoko Holder</Customer_Name>
		<Customer_Email>a.tortor@hotmail.net</Customer_Email>
		<Customer_Phone>(714) 218-8657</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-15</last_update>
	</record>
	<record>
		<Customer_PK>694</Customer_PK>
		<Customer_ID>739</Customer_ID>
		<Customer_Name>Kimberley Leach</Customer_Name>
		<Customer_Email>sed.orci@icloud.org</Customer_Email>
		<Customer_Phone>(274) 263-6706</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-19</last_update>
	</record>
	<record>
		<Customer_PK>695</Customer_PK>
		<Customer_ID>874</Customer_ID>
		<Customer_Name>Jessica Mullen</Customer_Name>
		<Customer_Email>imperdiet.non.vestibulum@google.couk</Customer_Email>
		<Customer_Phone>(264) 864-7387</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-10</last_update>
	</record>
	<record>
		<Customer_PK>696</Customer_PK>
		<Customer_ID>584</Customer_ID>
		<Customer_Name>Hadassah Rivers</Customer_Name>
		<Customer_Email>at@protonmail.couk</Customer_Email>
		<Customer_Phone>(392) 883-9865</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-23</last_update>
	</record>
	<record>
		<Customer_PK>697</Customer_PK>
		<Customer_ID>846</Customer_ID>
		<Customer_Name>David Dean</Customer_Name>
		<Customer_Email>ornare.tortor@hotmail.net</Customer_Email>
		<Customer_Phone>(427) 461-7811</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-5-2</last_update>
	</record>
	<record>
		<Customer_PK>698</Customer_PK>
		<Customer_ID>838</Customer_ID>
		<Customer_Name>Isabella Park</Customer_Name>
		<Customer_Email>tellus.suspendisse@aol.net</Customer_Email>
		<Customer_Phone>1-142-501-5887</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-13</last_update>
	</record>
	<record>
		<Customer_PK>699</Customer_PK>
		<Customer_ID>840</Customer_ID>
		<Customer_Name>Isadora Jarvis</Customer_Name>
		<Customer_Email>vehicula.risus@aol.edu</Customer_Email>
		<Customer_Phone>1-630-871-8524</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-13</last_update>
	</record>
	<record>
		<Customer_PK>700</Customer_PK>
		<Customer_ID>817</Customer_ID>
		<Customer_Name>August Aguirre</Customer_Name>
		<Customer_Email>magna.malesuada.vel@icloud.org</Customer_Email>
		<Customer_Phone>1-637-961-8114</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-23</last_update>
	</record>
	<record>
		<Customer_PK>701</Customer_PK>
		<Customer_ID>838</Customer_ID>
		<Customer_Name>Ivory Cline</Customer_Name>
		<Customer_Email>habitant.morbi@outlook.net</Customer_Email>
		<Customer_Phone>1-827-192-9245</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-5-18</last_update>
	</record>
	<record>
		<Customer_PK>702</Customer_PK>
		<Customer_ID>834</Customer_ID>
		<Customer_Name>Meredith Hudson</Customer_Name>
		<Customer_Email>massa.mauris@aol.ca</Customer_Email>
		<Customer_Phone>(395) 636-8667</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-25</last_update>
	</record>
	<record>
		<Customer_PK>703</Customer_PK>
		<Customer_ID>661</Customer_ID>
		<Customer_Name>Holly Delacruz</Customer_Name>
		<Customer_Email>semper.tellus.id@yahoo.edu</Customer_Email>
		<Customer_Phone>1-220-774-0284</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-8-31</last_update>
	</record>
	<record>
		<Customer_PK>704</Customer_PK>
		<Customer_ID>933</Customer_ID>
		<Customer_Name>Cynthia Acevedo</Customer_Name>
		<Customer_Email>nunc.interdum.feugiat@hotmail.net</Customer_Email>
		<Customer_Phone>(765) 547-7341</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-10-13</last_update>
	</record>
	<record>
		<Customer_PK>705</Customer_PK>
		<Customer_ID>583</Customer_ID>
		<Customer_Name>Bradley Greer</Customer_Name>
		<Customer_Email>nisl.quisque.fringilla@protonmail.edu</Customer_Email>
		<Customer_Phone>(818) 751-1273</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-7</last_update>
	</record>
	<record>
		<Customer_PK>706</Customer_PK>
		<Customer_ID>819</Customer_ID>
		<Customer_Name>Selma Atkinson</Customer_Name>
		<Customer_Email>mus.proin@aol.net</Customer_Email>
		<Customer_Phone>(376) 319-7348</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-5-2</last_update>
	</record>
	<record>
		<Customer_PK>707</Customer_PK>
		<Customer_ID>623</Customer_ID>
		<Customer_Name>Beck Combs</Customer_Name>
		<Customer_Email>nonummy.ipsum.non@icloud.org</Customer_Email>
		<Customer_Phone>1-295-867-1206</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-10-17</last_update>
	</record>
	<record>
		<Customer_PK>708</Customer_PK>
		<Customer_ID>504</Customer_ID>
		<Customer_Name>Darryl Gay</Customer_Name>
		<Customer_Email>nam.porttitor@yahoo.com</Customer_Email>
		<Customer_Phone>(758) 187-8353</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-8-17</last_update>
	</record>
	<record>
		<Customer_PK>709</Customer_PK>
		<Customer_ID>913</Customer_ID>
		<Customer_Name>Asher Bailey</Customer_Name>
		<Customer_Email>varius.orci@google.couk</Customer_Email>
		<Customer_Phone>1-571-375-4478</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-4-10</last_update>
	</record>
	<record>
		<Customer_PK>710</Customer_PK>
		<Customer_ID>865</Customer_ID>
		<Customer_Name>Chandler Avila</Customer_Name>
		<Customer_Email>risus.quisque@icloud.net</Customer_Email>
		<Customer_Phone>1-714-335-7145</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-4-21</last_update>
	</record>
	<record>
		<Customer_PK>711</Customer_PK>
		<Customer_ID>505</Customer_ID>
		<Customer_Name>Ray Hammond</Customer_Name>
		<Customer_Email>egestas@aol.com</Customer_Email>
		<Customer_Phone>1-481-216-3214</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-4-11</last_update>
	</record>
	<record>
		<Customer_PK>712</Customer_PK>
		<Customer_ID>934</Customer_ID>
		<Customer_Name>Hunter Rosales</Customer_Name>
		<Customer_Email>nunc.sed.pede@icloud.edu</Customer_Email>
		<Customer_Phone>(135) 775-3725</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-1-1</last_update>
	</record>
	<record>
		<Customer_PK>713</Customer_PK>
		<Customer_ID>762</Customer_ID>
		<Customer_Name>Flavia Dennis</Customer_Name>
		<Customer_Email>ac.eleifend@hotmail.com</Customer_Email>
		<Customer_Phone>(824) 388-8760</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-1</last_update>
	</record>
	<record>
		<Customer_PK>714</Customer_PK>
		<Customer_ID>596</Customer_ID>
		<Customer_Name>Honorato Welch</Customer_Name>
		<Customer_Email>vehicula@aol.edu</Customer_Email>
		<Customer_Phone>1-294-326-1558</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-27</last_update>
	</record>
	<record>
		<Customer_PK>715</Customer_PK>
		<Customer_ID>925</Customer_ID>
		<Customer_Name>Nissim Gonzalez</Customer_Name>
		<Customer_Email>lectus@google.org</Customer_Email>
		<Customer_Phone>1-915-276-5481</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-10</last_update>
	</record>
	<record>
		<Customer_PK>716</Customer_PK>
		<Customer_ID>602</Customer_ID>
		<Customer_Name>Kylan Palmer</Customer_Name>
		<Customer_Email>nascetur.ridiculus.mus@outlook.net</Customer_Email>
		<Customer_Phone>1-616-253-6053</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-9</last_update>
	</record>
	<record>
		<Customer_PK>717</Customer_PK>
		<Customer_ID>947</Customer_ID>
		<Customer_Name>Mark Willis</Customer_Name>
		<Customer_Email>mauris.aliquam@google.couk</Customer_Email>
		<Customer_Phone>1-697-648-1408</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-11</last_update>
	</record>
	<record>
		<Customer_PK>718</Customer_PK>
		<Customer_ID>554</Customer_ID>
		<Customer_Name>Yael Curry</Customer_Name>
		<Customer_Email>nibh@icloud.org</Customer_Email>
		<Customer_Phone>(578) 202-3116</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-10-30</last_update>
	</record>
	<record>
		<Customer_PK>719</Customer_PK>
		<Customer_ID>719</Customer_ID>
		<Customer_Name>Brock Frank</Customer_Name>
		<Customer_Email>dolor.nonummy.ac@protonmail.org</Customer_Email>
		<Customer_Phone>1-143-228-7712</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-23</last_update>
	</record>
	<record>
		<Customer_PK>720</Customer_PK>
		<Customer_ID>971</Customer_ID>
		<Customer_Name>MacKenzie Lang</Customer_Name>
		<Customer_Email>amet@outlook.net</Customer_Email>
		<Customer_Phone>1-659-282-9418</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-4-8</last_update>
	</record>
	<record>
		<Customer_PK>721</Customer_PK>
		<Customer_ID>885</Customer_ID>
		<Customer_Name>Reece Poole</Customer_Name>
		<Customer_Email>arcu@yahoo.com</Customer_Email>
		<Customer_Phone>1-437-442-8271</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-8-8</last_update>
	</record>
	<record>
		<Customer_PK>722</Customer_PK>
		<Customer_ID>706</Customer_ID>
		<Customer_Name>Bianca Atkinson</Customer_Name>
		<Customer_Email>amet@protonmail.couk</Customer_Email>
		<Customer_Phone>(388) 776-5287</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-3</last_update>
	</record>
	<record>
		<Customer_PK>723</Customer_PK>
		<Customer_ID>520</Customer_ID>
		<Customer_Name>Charity O'connor</Customer_Name>
		<Customer_Email>enim.consequat.purus@icloud.org</Customer_Email>
		<Customer_Phone>(226) 672-8722</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-9-28</last_update>
	</record>
	<record>
		<Customer_PK>724</Customer_PK>
		<Customer_ID>624</Customer_ID>
		<Customer_Name>Farrah Booker</Customer_Name>
		<Customer_Email>leo.morbi@hotmail.net</Customer_Email>
		<Customer_Phone>1-413-523-6786</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-20</last_update>
	</record>
	<record>
		<Customer_PK>725</Customer_PK>
		<Customer_ID>706</Customer_ID>
		<Customer_Name>Ann Bradford</Customer_Name>
		<Customer_Email>facilisis@outlook.org</Customer_Email>
		<Customer_Phone>1-875-827-2494</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-2-11</last_update>
	</record>
	<record>
		<Customer_PK>726</Customer_PK>
		<Customer_ID>834</Customer_ID>
		<Customer_Name>Flynn Pennington</Customer_Name>
		<Customer_Email>a.tortor@outlook.net</Customer_Email>
		<Customer_Phone>1-732-641-4443</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-13</last_update>
	</record>
	<record>
		<Customer_PK>727</Customer_PK>
		<Customer_ID>808</Customer_ID>
		<Customer_Name>Justina Pugh</Customer_Name>
		<Customer_Email>et.malesuada@google.couk</Customer_Email>
		<Customer_Phone>1-776-348-3725</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-6</last_update>
	</record>
	<record>
		<Customer_PK>728</Customer_PK>
		<Customer_ID>520</Customer_ID>
		<Customer_Name>Cassady Kaufman</Customer_Name>
		<Customer_Email>odio@aol.net</Customer_Email>
		<Customer_Phone>(641) 386-1671</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-9</last_update>
	</record>
	<record>
		<Customer_PK>729</Customer_PK>
		<Customer_ID>596</Customer_ID>
		<Customer_Name>Kessie Mclean</Customer_Name>
		<Customer_Email>mauris@icloud.couk</Customer_Email>
		<Customer_Phone>(558) 188-5885</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-19</last_update>
	</record>
	<record>
		<Customer_PK>730</Customer_PK>
		<Customer_ID>684</Customer_ID>
		<Customer_Name>Jameson Padilla</Customer_Name>
		<Customer_Email>vulputate.mauris@yahoo.com</Customer_Email>
		<Customer_Phone>1-688-158-5217</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-1</last_update>
	</record>
	<record>
		<Customer_PK>731</Customer_PK>
		<Customer_ID>539</Customer_ID>
		<Customer_Name>Zeph Rush</Customer_Name>
		<Customer_Email>nunc.mauris.morbi@protonmail.net</Customer_Email>
		<Customer_Phone>1-386-601-7362</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-4-8</last_update>
	</record>
	<record>
		<Customer_PK>732</Customer_PK>
		<Customer_ID>860</Customer_ID>
		<Customer_Name>Iliana Knowles</Customer_Name>
		<Customer_Email>sed.leo@aol.ca</Customer_Email>
		<Customer_Phone>(633) 149-5857</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-18</last_update>
	</record>
	<record>
		<Customer_PK>733</Customer_PK>
		<Customer_ID>840</Customer_ID>
		<Customer_Name>Halee Hernandez</Customer_Name>
		<Customer_Email>amet.ultricies.sem@yahoo.net</Customer_Email>
		<Customer_Phone>(393) 658-2163</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-5</last_update>
	</record>
	<record>
		<Customer_PK>734</Customer_PK>
		<Customer_ID>626</Customer_ID>
		<Customer_Name>Lara Horne</Customer_Name>
		<Customer_Email>a.ultricies@outlook.couk</Customer_Email>
		<Customer_Phone>1-512-482-7367</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-25</last_update>
	</record>
	<record>
		<Customer_PK>735</Customer_PK>
		<Customer_ID>986</Customer_ID>
		<Customer_Name>Erasmus Castaneda</Customer_Name>
		<Customer_Email>curae.donec@yahoo.org</Customer_Email>
		<Customer_Phone>(675) 543-4212</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-6</last_update>
	</record>
	<record>
		<Customer_PK>736</Customer_PK>
		<Customer_ID>514</Customer_ID>
		<Customer_Name>Todd Mason</Customer_Name>
		<Customer_Email>amet.faucibus.ut@outlook.couk</Customer_Email>
		<Customer_Phone>1-587-453-4412</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-2</last_update>
	</record>
	<record>
		<Customer_PK>737</Customer_PK>
		<Customer_ID>529</Customer_ID>
		<Customer_Name>Rajah French</Customer_Name>
		<Customer_Email>vivamus@aol.ca</Customer_Email>
		<Customer_Phone>1-261-625-7342</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-29</last_update>
	</record>
	<record>
		<Customer_PK>738</Customer_PK>
		<Customer_ID>777</Customer_ID>
		<Customer_Name>Nola Mullen</Customer_Name>
		<Customer_Email>a@icloud.ca</Customer_Email>
		<Customer_Phone>(565) 671-4368</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-5</last_update>
	</record>
	<record>
		<Customer_PK>739</Customer_PK>
		<Customer_ID>653</Customer_ID>
		<Customer_Name>Burton Cain</Customer_Name>
		<Customer_Email>velit@icloud.net</Customer_Email>
		<Customer_Phone>1-216-224-3257</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-20</last_update>
	</record>
	<record>
		<Customer_PK>740</Customer_PK>
		<Customer_ID>908</Customer_ID>
		<Customer_Name>Wendy Conner</Customer_Name>
		<Customer_Email>velit.dui@outlook.edu</Customer_Email>
		<Customer_Phone>(843) 451-1142</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-24</last_update>
	</record>
	<record>
		<Customer_PK>741</Customer_PK>
		<Customer_ID>590</Customer_ID>
		<Customer_Name>Jasper Gay</Customer_Name>
		<Customer_Email>vitae@hotmail.ca</Customer_Email>
		<Customer_Phone>(302) 667-1113</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-15</last_update>
	</record>
	<record>
		<Customer_PK>742</Customer_PK>
		<Customer_ID>506</Customer_ID>
		<Customer_Name>Finn Gamble</Customer_Name>
		<Customer_Email>habitant.morbi@google.net</Customer_Email>
		<Customer_Phone>(733) 873-2117</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-10-4</last_update>
	</record>
	<record>
		<Customer_PK>743</Customer_PK>
		<Customer_ID>605</Customer_ID>
		<Customer_Name>Dalton Sykes</Customer_Name>
		<Customer_Email>iaculis.quis@aol.org</Customer_Email>
		<Customer_Phone>1-649-862-2414</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-16</last_update>
	</record>
	<record>
		<Customer_PK>744</Customer_PK>
		<Customer_ID>608</Customer_ID>
		<Customer_Name>Connor Tanner</Customer_Name>
		<Customer_Email>risus.donec@outlook.com</Customer_Email>
		<Customer_Phone>(542) 682-7688</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-19</last_update>
	</record>
	<record>
		<Customer_PK>745</Customer_PK>
		<Customer_ID>516</Customer_ID>
		<Customer_Name>Amber Booker</Customer_Name>
		<Customer_Email>mus.proin.vel@protonmail.couk</Customer_Email>
		<Customer_Phone>(640) 171-7672</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-19</last_update>
	</record>
	<record>
		<Customer_PK>746</Customer_PK>
		<Customer_ID>993</Customer_ID>
		<Customer_Name>Alika Solomon</Customer_Name>
		<Customer_Email>diam.vel.arcu@protonmail.net</Customer_Email>
		<Customer_Phone>1-742-402-0741</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-4</last_update>
	</record>
	<record>
		<Customer_PK>747</Customer_PK>
		<Customer_ID>687</Customer_ID>
		<Customer_Name>Channing Whitehead</Customer_Name>
		<Customer_Email>lectus.quis.massa@aol.couk</Customer_Email>
		<Customer_Phone>(276) 745-7238</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-25</last_update>
	</record>
	<record>
		<Customer_PK>748</Customer_PK>
		<Customer_ID>619</Customer_ID>
		<Customer_Name>Nita Simpson</Customer_Name>
		<Customer_Email>egestas.duis@yahoo.couk</Customer_Email>
		<Customer_Phone>1-637-367-5154</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-17</last_update>
	</record>
	<record>
		<Customer_PK>749</Customer_PK>
		<Customer_ID>820</Customer_ID>
		<Customer_Name>Lyle Barker</Customer_Name>
		<Customer_Email>quisque.ornare@aol.org</Customer_Email>
		<Customer_Phone>(761) 966-7337</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-17</last_update>
	</record>
	<record>
		<Customer_PK>750</Customer_PK>
		<Customer_ID>653</Customer_ID>
		<Customer_Name>Lars Acevedo</Customer_Name>
		<Customer_Email>diam.vel.arcu@google.com</Customer_Email>
		<Customer_Phone>(429) 623-1066</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-28</last_update>
	</record>
	<record>
		<Customer_PK>751</Customer_PK>
		<Customer_ID>974</Customer_ID>
		<Customer_Name>Camden Greer</Customer_Name>
		<Customer_Email>vitae@icloud.com</Customer_Email>
		<Customer_Phone>(978) 524-8593</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-20</last_update>
	</record>
	<record>
		<Customer_PK>752</Customer_PK>
		<Customer_ID>669</Customer_ID>
		<Customer_Name>Ila Holman</Customer_Name>
		<Customer_Email>vivamus.sit.amet@aol.edu</Customer_Email>
		<Customer_Phone>(478) 758-4532</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-9</last_update>
	</record>
	<record>
		<Customer_PK>753</Customer_PK>
		<Customer_ID>634</Customer_ID>
		<Customer_Name>Genevieve Cummings</Customer_Name>
		<Customer_Email>facilisis@aol.couk</Customer_Email>
		<Customer_Phone>(755) 572-9251</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-11-24</last_update>
	</record>
	<record>
		<Customer_PK>754</Customer_PK>
		<Customer_ID>627</Customer_ID>
		<Customer_Name>Rosalyn Ramirez</Customer_Name>
		<Customer_Email>nec.ante.blandit@google.edu</Customer_Email>
		<Customer_Phone>(585) 601-1376</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-2</last_update>
	</record>
	<record>
		<Customer_PK>755</Customer_PK>
		<Customer_ID>514</Customer_ID>
		<Customer_Name>Marshall Kennedy</Customer_Name>
		<Customer_Email>nunc.risus@yahoo.net</Customer_Email>
		<Customer_Phone>(927) 765-9014</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-11-27</last_update>
	</record>
	<record>
		<Customer_PK>756</Customer_PK>
		<Customer_ID>950</Customer_ID>
		<Customer_Name>Cain Nguyen</Customer_Name>
		<Customer_Email>et@yahoo.com</Customer_Email>
		<Customer_Phone>1-401-502-7486</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-9-9</last_update>
	</record>
	<record>
		<Customer_PK>757</Customer_PK>
		<Customer_ID>597</Customer_ID>
		<Customer_Name>Kaye Moore</Customer_Name>
		<Customer_Email>conubia@icloud.ca</Customer_Email>
		<Customer_Phone>(112) 979-3886</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-11</last_update>
	</record>
	<record>
		<Customer_PK>758</Customer_PK>
		<Customer_ID>982</Customer_ID>
		<Customer_Name>Yvette Glenn</Customer_Name>
		<Customer_Email>nunc.sollicitudin@yahoo.ca</Customer_Email>
		<Customer_Phone>1-226-622-5268</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-18</last_update>
	</record>
	<record>
		<Customer_PK>759</Customer_PK>
		<Customer_ID>711</Customer_ID>
		<Customer_Name>Leroy Lewis</Customer_Name>
		<Customer_Email>hendrerit.consectetuer.cursus@google.net</Customer_Email>
		<Customer_Phone>1-273-837-8662</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-19</last_update>
	</record>
	<record>
		<Customer_PK>760</Customer_PK>
		<Customer_ID>956</Customer_ID>
		<Customer_Name>Yoko Lucas</Customer_Name>
		<Customer_Email>non.dapibus@aol.edu</Customer_Email>
		<Customer_Phone>1-135-634-6366</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-11-3</last_update>
	</record>
	<record>
		<Customer_PK>761</Customer_PK>
		<Customer_ID>951</Customer_ID>
		<Customer_Name>Medge Mcfadden</Customer_Name>
		<Customer_Email>urna@hotmail.net</Customer_Email>
		<Customer_Phone>(372) 363-0859</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-16</last_update>
	</record>
	<record>
		<Customer_PK>762</Customer_PK>
		<Customer_ID>568</Customer_ID>
		<Customer_Name>Ashton Gallagher</Customer_Name>
		<Customer_Email>lorem.ipsum@aol.couk</Customer_Email>
		<Customer_Phone>(353) 257-5445</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-14</last_update>
	</record>
	<record>
		<Customer_PK>763</Customer_PK>
		<Customer_ID>846</Customer_ID>
		<Customer_Name>Faith Bishop</Customer_Name>
		<Customer_Email>tortor.nunc@google.org</Customer_Email>
		<Customer_Phone>(247) 757-5488</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-23</last_update>
	</record>
	<record>
		<Customer_PK>764</Customer_PK>
		<Customer_ID>503</Customer_ID>
		<Customer_Name>Stuart Joyce</Customer_Name>
		<Customer_Email>vitae.mauris@hotmail.net</Customer_Email>
		<Customer_Phone>(645) 476-1378</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-7</last_update>
	</record>
	<record>
		<Customer_PK>765</Customer_PK>
		<Customer_ID>604</Customer_ID>
		<Customer_Name>Rebecca Goodwin</Customer_Name>
		<Customer_Email>morbi@yahoo.ca</Customer_Email>
		<Customer_Phone>(427) 844-3458</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-8</last_update>
	</record>
	<record>
		<Customer_PK>766</Customer_PK>
		<Customer_ID>967</Customer_ID>
		<Customer_Name>Orla Byrd</Customer_Name>
		<Customer_Email>mollis.non.cursus@outlook.couk</Customer_Email>
		<Customer_Phone>1-769-721-6450</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-21</last_update>
	</record>
	<record>
		<Customer_PK>767</Customer_PK>
		<Customer_ID>508</Customer_ID>
		<Customer_Name>Kermit Perkins</Customer_Name>
		<Customer_Email>non.arcu@yahoo.edu</Customer_Email>
		<Customer_Phone>(626) 414-1682</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-1</last_update>
	</record>
	<record>
		<Customer_PK>768</Customer_PK>
		<Customer_ID>701</Customer_ID>
		<Customer_Name>Maile Bean</Customer_Name>
		<Customer_Email>ornare.elit.elit@icloud.ca</Customer_Email>
		<Customer_Phone>(318) 483-4667</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-20</last_update>
	</record>
	<record>
		<Customer_PK>769</Customer_PK>
		<Customer_ID>928</Customer_ID>
		<Customer_Name>Jessamine Harper</Customer_Name>
		<Customer_Email>torquent.per@protonmail.com</Customer_Email>
		<Customer_Phone>1-167-949-1686</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-5</last_update>
	</record>
	<record>
		<Customer_PK>770</Customer_PK>
		<Customer_ID>932</Customer_ID>
		<Customer_Name>Chaney Bray</Customer_Name>
		<Customer_Email>neque.sed.sem@hotmail.com</Customer_Email>
		<Customer_Phone>(332) 186-4037</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-6</last_update>
	</record>
	<record>
		<Customer_PK>771</Customer_PK>
		<Customer_ID>812</Customer_ID>
		<Customer_Name>Gavin Hicks</Customer_Name>
		<Customer_Email>scelerisque@yahoo.net</Customer_Email>
		<Customer_Phone>1-856-824-1109</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-11-16</last_update>
	</record>
	<record>
		<Customer_PK>772</Customer_PK>
		<Customer_ID>619</Customer_ID>
		<Customer_Name>Alika Clay</Customer_Name>
		<Customer_Email>ut.ipsum@outlook.edu</Customer_Email>
		<Customer_Phone>1-953-872-1146</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-14</last_update>
	</record>
	<record>
		<Customer_PK>773</Customer_PK>
		<Customer_ID>625</Customer_ID>
		<Customer_Name>Reece Bowers</Customer_Name>
		<Customer_Email>viverra@hotmail.couk</Customer_Email>
		<Customer_Phone>(922) 207-1513</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-21</last_update>
	</record>
	<record>
		<Customer_PK>774</Customer_PK>
		<Customer_ID>944</Customer_ID>
		<Customer_Name>Malik Macdonald</Customer_Name>
		<Customer_Email>non.leo@icloud.couk</Customer_Email>
		<Customer_Phone>1-374-331-8271</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-7</last_update>
	</record>
	<record>
		<Customer_PK>775</Customer_PK>
		<Customer_ID>734</Customer_ID>
		<Customer_Name>Elvis Harvey</Customer_Name>
		<Customer_Email>neque.non@google.ca</Customer_Email>
		<Customer_Phone>(972) 692-7117</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-1</last_update>
	</record>
	<record>
		<Customer_PK>776</Customer_PK>
		<Customer_ID>940</Customer_ID>
		<Customer_Name>Abra Roth</Customer_Name>
		<Customer_Email>commodo.ipsum@hotmail.org</Customer_Email>
		<Customer_Phone>1-976-354-9790</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-8</last_update>
	</record>
	<record>
		<Customer_PK>777</Customer_PK>
		<Customer_ID>561</Customer_ID>
		<Customer_Name>Charissa Knapp</Customer_Name>
		<Customer_Email>rutrum@outlook.couk</Customer_Email>
		<Customer_Phone>(460) 752-1656</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-16</last_update>
	</record>
	<record>
		<Customer_PK>778</Customer_PK>
		<Customer_ID>658</Customer_ID>
		<Customer_Name>Wilma Baldwin</Customer_Name>
		<Customer_Email>nisi@yahoo.edu</Customer_Email>
		<Customer_Phone>1-476-875-5597</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-22</last_update>
	</record>
	<record>
		<Customer_PK>779</Customer_PK>
		<Customer_ID>844</Customer_ID>
		<Customer_Name>Emery Allison</Customer_Name>
		<Customer_Email>vehicula.pellentesque.tincidunt@hotmail.ca</Customer_Email>
		<Customer_Phone>(725) 273-7322</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-10-24</last_update>
	</record>
	<record>
		<Customer_PK>780</Customer_PK>
		<Customer_ID>924</Customer_ID>
		<Customer_Name>Nina Hodges</Customer_Name>
		<Customer_Email>pharetra.quisque.ac@yahoo.ca</Customer_Email>
		<Customer_Phone>1-641-623-8839</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-10</last_update>
	</record>
	<record>
		<Customer_PK>781</Customer_PK>
		<Customer_ID>987</Customer_ID>
		<Customer_Name>Jacob Coffey</Customer_Name>
		<Customer_Email>lorem.eu@outlook.ca</Customer_Email>
		<Customer_Phone>1-701-271-3726</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-25</last_update>
	</record>
	<record>
		<Customer_PK>782</Customer_PK>
		<Customer_ID>527</Customer_ID>
		<Customer_Name>Shea Potts</Customer_Name>
		<Customer_Email>at.iaculis@outlook.org</Customer_Email>
		<Customer_Phone>(480) 289-8646</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-25</last_update>
	</record>
	<record>
		<Customer_PK>783</Customer_PK>
		<Customer_ID>832</Customer_ID>
		<Customer_Name>Giacomo Holland</Customer_Name>
		<Customer_Email>arcu@outlook.ca</Customer_Email>
		<Customer_Phone>(633) 228-2684</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-18</last_update>
	</record>
	<record>
		<Customer_PK>784</Customer_PK>
		<Customer_ID>613</Customer_ID>
		<Customer_Name>Marvin Baldwin</Customer_Name>
		<Customer_Email>placerat.orci@hotmail.org</Customer_Email>
		<Customer_Phone>1-659-412-3228</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-6</last_update>
	</record>
	<record>
		<Customer_PK>785</Customer_PK>
		<Customer_ID>595</Customer_ID>
		<Customer_Name>Melissa Mcbride</Customer_Name>
		<Customer_Email>enim.non@outlook.couk</Customer_Email>
		<Customer_Phone>(274) 209-1583</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-31</last_update>
	</record>
	<record>
		<Customer_PK>786</Customer_PK>
		<Customer_ID>745</Customer_ID>
		<Customer_Name>Geoffrey Gordon</Customer_Name>
		<Customer_Email>in.faucibus@aol.couk</Customer_Email>
		<Customer_Phone>1-312-984-6845</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-17</last_update>
	</record>
	<record>
		<Customer_PK>787</Customer_PK>
		<Customer_ID>967</Customer_ID>
		<Customer_Name>Yuli Bullock</Customer_Name>
		<Customer_Email>hendrerit.a.arcu@aol.edu</Customer_Email>
		<Customer_Phone>(770) 985-4615</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-14</last_update>
	</record>
	<record>
		<Customer_PK>788</Customer_PK>
		<Customer_ID>602</Customer_ID>
		<Customer_Name>Nicholas Lopez</Customer_Name>
		<Customer_Email>augue@aol.edu</Customer_Email>
		<Customer_Phone>(571) 523-2439</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-9</last_update>
	</record>
	<record>
		<Customer_PK>789</Customer_PK>
		<Customer_ID>584</Customer_ID>
		<Customer_Name>Amity Grant</Customer_Name>
		<Customer_Email>sagittis@google.org</Customer_Email>
		<Customer_Phone>1-341-431-6406</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-10</last_update>
	</record>
	<record>
		<Customer_PK>790</Customer_PK>
		<Customer_ID>759</Customer_ID>
		<Customer_Name>Wendy Murphy</Customer_Name>
		<Customer_Email>molestie.in@google.org</Customer_Email>
		<Customer_Phone>(383) 508-7206</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-14</last_update>
	</record>
	<record>
		<Customer_PK>791</Customer_PK>
		<Customer_ID>974</Customer_ID>
		<Customer_Name>Warren Robertson</Customer_Name>
		<Customer_Email>sit.amet.risus@icloud.couk</Customer_Email>
		<Customer_Phone>1-905-568-6875</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-23</last_update>
	</record>
	<record>
		<Customer_PK>792</Customer_PK>
		<Customer_ID>591</Customer_ID>
		<Customer_Name>Gail Smith</Customer_Name>
		<Customer_Email>nec.metus@google.couk</Customer_Email>
		<Customer_Phone>1-231-857-2141</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-8-29</last_update>
	</record>
	<record>
		<Customer_PK>793</Customer_PK>
		<Customer_ID>738</Customer_ID>
		<Customer_Name>Ignatius Golden</Customer_Name>
		<Customer_Email>arcu@outlook.edu</Customer_Email>
		<Customer_Phone>1-963-331-8192</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-11-21</last_update>
	</record>
	<record>
		<Customer_PK>794</Customer_PK>
		<Customer_ID>738</Customer_ID>
		<Customer_Name>Leah Avery</Customer_Name>
		<Customer_Email>nisi.sem.semper@aol.org</Customer_Email>
		<Customer_Phone>1-338-812-4413</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-18</last_update>
	</record>
	<record>
		<Customer_PK>795</Customer_PK>
		<Customer_ID>887</Customer_ID>
		<Customer_Name>Jameson Boyd</Customer_Name>
		<Customer_Email>integer.in@yahoo.net</Customer_Email>
		<Customer_Phone>(471) 328-3986</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-26</last_update>
	</record>
	<record>
		<Customer_PK>796</Customer_PK>
		<Customer_ID>688</Customer_ID>
		<Customer_Name>Lilah House</Customer_Name>
		<Customer_Email>nulla.semper@yahoo.couk</Customer_Email>
		<Customer_Phone>(822) 480-2386</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-23</last_update>
	</record>
	<record>
		<Customer_PK>797</Customer_PK>
		<Customer_ID>854</Customer_ID>
		<Customer_Name>Tara Ashley</Customer_Name>
		<Customer_Email>nibh.lacinia@hotmail.com</Customer_Email>
		<Customer_Phone>1-326-813-7666</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-8</last_update>
	</record>
	<record>
		<Customer_PK>798</Customer_PK>
		<Customer_ID>978</Customer_ID>
		<Customer_Name>Josephine Glenn</Customer_Name>
		<Customer_Email>eu.eleifend@yahoo.ca</Customer_Email>
		<Customer_Phone>1-783-576-3742</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-15</last_update>
	</record>
	<record>
		<Customer_PK>799</Customer_PK>
		<Customer_ID>768</Customer_ID>
		<Customer_Name>David Holloway</Customer_Name>
		<Customer_Email>fringilla.ornare.placerat@protonmail.ca</Customer_Email>
		<Customer_Phone>1-787-365-3005</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-3</last_update>
	</record>
	<record>
		<Customer_PK>800</Customer_PK>
		<Customer_ID>580</Customer_ID>
		<Customer_Name>Michael Foley</Customer_Name>
		<Customer_Email>posuere.enim@yahoo.ca</Customer_Email>
		<Customer_Phone>(320) 738-9835</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-18</last_update>
	</record>
	<record>
		<Customer_PK>801</Customer_PK>
		<Customer_ID>929</Customer_ID>
		<Customer_Name>Vivian Glover</Customer_Name>
		<Customer_Email>ipsum.primis.in@aol.ca</Customer_Email>
		<Customer_Phone>(940) 918-9235</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-26</last_update>
	</record>
	<record>
		<Customer_PK>802</Customer_PK>
		<Customer_ID>830</Customer_ID>
		<Customer_Name>Nerea Santos</Customer_Name>
		<Customer_Email>eleifend.nunc.risus@aol.couk</Customer_Email>
		<Customer_Phone>(267) 833-8652</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-15</last_update>
	</record>
	<record>
		<Customer_PK>803</Customer_PK>
		<Customer_ID>676</Customer_ID>
		<Customer_Name>Gage Berry</Customer_Name>
		<Customer_Email>eleifend.vitae@google.org</Customer_Email>
		<Customer_Phone>(529) 843-3747</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-29</last_update>
	</record>
	<record>
		<Customer_PK>804</Customer_PK>
		<Customer_ID>809</Customer_ID>
		<Customer_Name>Linda Berg</Customer_Name>
		<Customer_Email>hendrerit.id@icloud.couk</Customer_Email>
		<Customer_Phone>(998) 142-4131</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-20</last_update>
	</record>
	<record>
		<Customer_PK>805</Customer_PK>
		<Customer_ID>549</Customer_ID>
		<Customer_Name>Myles Kline</Customer_Name>
		<Customer_Email>egestas@protonmail.couk</Customer_Email>
		<Customer_Phone>1-522-746-2574</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-2-26</last_update>
	</record>
	<record>
		<Customer_PK>806</Customer_PK>
		<Customer_ID>851</Customer_ID>
		<Customer_Name>Sonia Johnson</Customer_Name>
		<Customer_Email>urna.vivamus.molestie@yahoo.couk</Customer_Email>
		<Customer_Phone>(216) 187-8253</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-17</last_update>
	</record>
	<record>
		<Customer_PK>807</Customer_PK>
		<Customer_ID>630</Customer_ID>
		<Customer_Name>Henry Dodson</Customer_Name>
		<Customer_Email>nonummy.ac@outlook.net</Customer_Email>
		<Customer_Phone>(326) 314-5438</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-11-7</last_update>
	</record>
	<record>
		<Customer_PK>808</Customer_PK>
		<Customer_ID>500</Customer_ID>
		<Customer_Name>Jemima Ferrell</Customer_Name>
		<Customer_Email>vitae@hotmail.ca</Customer_Email>
		<Customer_Phone>(340) 976-7221</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-21</last_update>
	</record>
	<record>
		<Customer_PK>809</Customer_PK>
		<Customer_ID>667</Customer_ID>
		<Customer_Name>Owen Houston</Customer_Name>
		<Customer_Email>vestibulum.mauris@hotmail.com</Customer_Email>
		<Customer_Phone>1-273-869-4710</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-5-9</last_update>
	</record>
	<record>
		<Customer_PK>810</Customer_PK>
		<Customer_ID>615</Customer_ID>
		<Customer_Name>Desirae Harper</Customer_Name>
		<Customer_Email>integer@google.com</Customer_Email>
		<Customer_Phone>(374) 826-5686</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-8-23</last_update>
	</record>
	<record>
		<Customer_PK>811</Customer_PK>
		<Customer_ID>677</Customer_ID>
		<Customer_Name>Lars Britt</Customer_Name>
		<Customer_Email>enim.mi.tempor@outlook.net</Customer_Email>
		<Customer_Phone>1-682-358-6202</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-4</last_update>
	</record>
	<record>
		<Customer_PK>812</Customer_PK>
		<Customer_ID>584</Customer_ID>
		<Customer_Name>Isabelle Decker</Customer_Name>
		<Customer_Email>ipsum.phasellus@aol.org</Customer_Email>
		<Customer_Phone>1-845-107-7862</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-24</last_update>
	</record>
	<record>
		<Customer_PK>813</Customer_PK>
		<Customer_ID>776</Customer_ID>
		<Customer_Name>Emmanuel Hinton</Customer_Name>
		<Customer_Email>posuere.cubilia.curae@google.edu</Customer_Email>
		<Customer_Phone>(490) 656-6889</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-3</last_update>
	</record>
	<record>
		<Customer_PK>814</Customer_PK>
		<Customer_ID>636</Customer_ID>
		<Customer_Name>Hop Mcgowan</Customer_Name>
		<Customer_Email>donec.elementum@hotmail.org</Customer_Email>
		<Customer_Phone>1-656-272-6538</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-28</last_update>
	</record>
	<record>
		<Customer_PK>815</Customer_PK>
		<Customer_ID>656</Customer_ID>
		<Customer_Name>Amber Aguirre</Customer_Name>
		<Customer_Email>eu.ultrices@hotmail.couk</Customer_Email>
		<Customer_Phone>(315) 998-3274</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-1</last_update>
	</record>
	<record>
		<Customer_PK>816</Customer_PK>
		<Customer_ID>830</Customer_ID>
		<Customer_Name>Gwendolyn Warner</Customer_Name>
		<Customer_Email>et.ipsum.cursus@hotmail.edu</Customer_Email>
		<Customer_Phone>1-519-220-8575</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-8</last_update>
	</record>
	<record>
		<Customer_PK>817</Customer_PK>
		<Customer_ID>600</Customer_ID>
		<Customer_Name>Colt Butler</Customer_Name>
		<Customer_Email>dictum.augue@aol.com</Customer_Email>
		<Customer_Phone>(712) 855-6860</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-31</last_update>
	</record>
	<record>
		<Customer_PK>818</Customer_PK>
		<Customer_ID>787</Customer_ID>
		<Customer_Name>Brett Boone</Customer_Name>
		<Customer_Email>semper.nam.tempor@outlook.org</Customer_Email>
		<Customer_Phone>(138) 574-4917</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-22</last_update>
	</record>
	<record>
		<Customer_PK>819</Customer_PK>
		<Customer_ID>978</Customer_ID>
		<Customer_Name>Hunter Sharpe</Customer_Name>
		<Customer_Email>eget.laoreet.posuere@yahoo.net</Customer_Email>
		<Customer_Phone>(261) 781-6410</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-2</last_update>
	</record>
	<record>
		<Customer_PK>820</Customer_PK>
		<Customer_ID>538</Customer_ID>
		<Customer_Name>Phillip Woods</Customer_Name>
		<Customer_Email>aliquam.eu@hotmail.com</Customer_Email>
		<Customer_Phone>(917) 738-5890</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-22</last_update>
	</record>
	<record>
		<Customer_PK>821</Customer_PK>
		<Customer_ID>898</Customer_ID>
		<Customer_Name>Gretchen Dennis</Customer_Name>
		<Customer_Email>ullamcorper.velit.in@protonmail.couk</Customer_Email>
		<Customer_Phone>(395) 526-8047</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-11</last_update>
	</record>
	<record>
		<Customer_PK>822</Customer_PK>
		<Customer_ID>887</Customer_ID>
		<Customer_Name>Randall Livingston</Customer_Name>
		<Customer_Email>etiam.gravida@icloud.couk</Customer_Email>
		<Customer_Phone>1-331-318-7462</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-11-18</last_update>
	</record>
	<record>
		<Customer_PK>823</Customer_PK>
		<Customer_ID>845</Customer_ID>
		<Customer_Name>Audrey Guy</Customer_Name>
		<Customer_Email>nascetur@outlook.ca</Customer_Email>
		<Customer_Phone>1-446-510-8671</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-19</last_update>
	</record>
	<record>
		<Customer_PK>824</Customer_PK>
		<Customer_ID>737</Customer_ID>
		<Customer_Name>Minerva Davis</Customer_Name>
		<Customer_Email>pede.suspendisse.dui@yahoo.net</Customer_Email>
		<Customer_Phone>1-682-642-8067</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-20</last_update>
	</record>
	<record>
		<Customer_PK>825</Customer_PK>
		<Customer_ID>816</Customer_ID>
		<Customer_Name>Dai Herman</Customer_Name>
		<Customer_Email>et.magnis@yahoo.edu</Customer_Email>
		<Customer_Phone>(185) 886-0357</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-25</last_update>
	</record>
	<record>
		<Customer_PK>826</Customer_PK>
		<Customer_ID>755</Customer_ID>
		<Customer_Name>Griffith Barry</Customer_Name>
		<Customer_Email>semper@protonmail.couk</Customer_Email>
		<Customer_Phone>(320) 361-1523</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-5-23</last_update>
	</record>
	<record>
		<Customer_PK>827</Customer_PK>
		<Customer_ID>543</Customer_ID>
		<Customer_Name>Drake Hudson</Customer_Name>
		<Customer_Email>cras.lorem@protonmail.ca</Customer_Email>
		<Customer_Phone>1-562-864-9886</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-4-21</last_update>
	</record>
	<record>
		<Customer_PK>828</Customer_PK>
		<Customer_ID>919</Customer_ID>
		<Customer_Name>Delilah Francis</Customer_Name>
		<Customer_Email>dis@protonmail.ca</Customer_Email>
		<Customer_Phone>1-522-205-5266</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-31</last_update>
	</record>
	<record>
		<Customer_PK>829</Customer_PK>
		<Customer_ID>907</Customer_ID>
		<Customer_Name>Graiden Mcdaniel</Customer_Name>
		<Customer_Email>sagittis.lobortis@outlook.net</Customer_Email>
		<Customer_Phone>(117) 507-6679</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-10</last_update>
	</record>
	<record>
		<Customer_PK>830</Customer_PK>
		<Customer_ID>959</Customer_ID>
		<Customer_Name>Brendan Floyd</Customer_Name>
		<Customer_Email>sed.eu@google.net</Customer_Email>
		<Customer_Phone>1-333-910-1281</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-4-10</last_update>
	</record>
	<record>
		<Customer_PK>831</Customer_PK>
		<Customer_ID>980</Customer_ID>
		<Customer_Name>Kirby Beach</Customer_Name>
		<Customer_Email>sit.amet@protonmail.ca</Customer_Email>
		<Customer_Phone>1-263-522-8115</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-5-10</last_update>
	</record>
	<record>
		<Customer_PK>832</Customer_PK>
		<Customer_ID>606</Customer_ID>
		<Customer_Name>Charity Dixon</Customer_Name>
		<Customer_Email>integer.eu@yahoo.net</Customer_Email>
		<Customer_Phone>1-647-335-5098</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-11-4</last_update>
	</record>
	<record>
		<Customer_PK>833</Customer_PK>
		<Customer_ID>943</Customer_ID>
		<Customer_Name>Haley Eaton</Customer_Name>
		<Customer_Email>diam@icloud.edu</Customer_Email>
		<Customer_Phone>(311) 577-3183</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-4</last_update>
	</record>
	<record>
		<Customer_PK>834</Customer_PK>
		<Customer_ID>502</Customer_ID>
		<Customer_Name>William Keith</Customer_Name>
		<Customer_Email>nec.ligula@outlook.com</Customer_Email>
		<Customer_Phone>1-433-869-1349</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-12</last_update>
	</record>
	<record>
		<Customer_PK>835</Customer_PK>
		<Customer_ID>673</Customer_ID>
		<Customer_Name>Yvonne Daniels</Customer_Name>
		<Customer_Email>neque.vitae@google.org</Customer_Email>
		<Customer_Phone>(673) 933-2581</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-23</last_update>
	</record>
	<record>
		<Customer_PK>836</Customer_PK>
		<Customer_ID>762</Customer_ID>
		<Customer_Name>Hope Rollins</Customer_Name>
		<Customer_Email>nunc.commodo@yahoo.net</Customer_Email>
		<Customer_Phone>1-343-595-4220</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-18</last_update>
	</record>
	<record>
		<Customer_PK>837</Customer_PK>
		<Customer_ID>530</Customer_ID>
		<Customer_Name>Judith Buchanan</Customer_Name>
		<Customer_Email>consequat.auctor@protonmail.couk</Customer_Email>
		<Customer_Phone>1-479-884-7074</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-10</last_update>
	</record>
	<record>
		<Customer_PK>838</Customer_PK>
		<Customer_ID>547</Customer_ID>
		<Customer_Name>Buckminster Lowe</Customer_Name>
		<Customer_Email>sed.auctor@icloud.edu</Customer_Email>
		<Customer_Phone>(582) 911-4514</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-23</last_update>
	</record>
	<record>
		<Customer_PK>839</Customer_PK>
		<Customer_ID>957</Customer_ID>
		<Customer_Name>Yvette Juarez</Customer_Name>
		<Customer_Email>at.pede@aol.couk</Customer_Email>
		<Customer_Phone>(217) 673-4523</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-3</last_update>
	</record>
	<record>
		<Customer_PK>840</Customer_PK>
		<Customer_ID>988</Customer_ID>
		<Customer_Name>Forrest Santana</Customer_Name>
		<Customer_Email>aliquam.nisl@icloud.edu</Customer_Email>
		<Customer_Phone>(821) 546-6981</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-12</last_update>
	</record>
	<record>
		<Customer_PK>841</Customer_PK>
		<Customer_ID>988</Customer_ID>
		<Customer_Name>Dane Sellers</Customer_Name>
		<Customer_Email>elit.curabitur.sed@yahoo.com</Customer_Email>
		<Customer_Phone>1-846-632-6534</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-8-20</last_update>
	</record>
	<record>
		<Customer_PK>842</Customer_PK>
		<Customer_ID>810</Customer_ID>
		<Customer_Name>Fitzgerald Odom</Customer_Name>
		<Customer_Email>sed.turpis@outlook.com</Customer_Email>
		<Customer_Phone>1-239-573-8447</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-2-13</last_update>
	</record>
	<record>
		<Customer_PK>843</Customer_PK>
		<Customer_ID>873</Customer_ID>
		<Customer_Name>Melvin Clemons</Customer_Name>
		<Customer_Email>consequat.enim.diam@yahoo.com</Customer_Email>
		<Customer_Phone>1-618-868-7558</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-20</last_update>
	</record>
	<record>
		<Customer_PK>844</Customer_PK>
		<Customer_ID>578</Customer_ID>
		<Customer_Name>Cherokee Waller</Customer_Name>
		<Customer_Email>ligula.donec@protonmail.net</Customer_Email>
		<Customer_Phone>1-967-514-4761</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-14</last_update>
	</record>
	<record>
		<Customer_PK>845</Customer_PK>
		<Customer_ID>541</Customer_ID>
		<Customer_Name>Lael Stevens</Customer_Name>
		<Customer_Email>a.arcu@hotmail.org</Customer_Email>
		<Customer_Phone>1-268-144-7488</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-26</last_update>
	</record>
	<record>
		<Customer_PK>846</Customer_PK>
		<Customer_ID>546</Customer_ID>
		<Customer_Name>Nelle Bowman</Customer_Name>
		<Customer_Email>etiam.gravida@icloud.org</Customer_Email>
		<Customer_Phone>(331) 960-3357</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-11-6</last_update>
	</record>
	<record>
		<Customer_PK>847</Customer_PK>
		<Customer_ID>938</Customer_ID>
		<Customer_Name>Carl Morales</Customer_Name>
		<Customer_Email>fringilla.donec.feugiat@hotmail.org</Customer_Email>
		<Customer_Phone>(490) 363-1260</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-21</last_update>
	</record>
	<record>
		<Customer_PK>848</Customer_PK>
		<Customer_ID>643</Customer_ID>
		<Customer_Name>Allen Henry</Customer_Name>
		<Customer_Email>nulla.integer@yahoo.ca</Customer_Email>
		<Customer_Phone>1-231-812-6877</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-25</last_update>
	</record>
	<record>
		<Customer_PK>849</Customer_PK>
		<Customer_ID>717</Customer_ID>
		<Customer_Name>Maxine Rodgers</Customer_Name>
		<Customer_Email>facilisis.facilisis@outlook.net</Customer_Email>
		<Customer_Phone>(853) 346-0274</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-11-6</last_update>
	</record>
	<record>
		<Customer_PK>850</Customer_PK>
		<Customer_ID>965</Customer_ID>
		<Customer_Name>Kareem Chandler</Customer_Name>
		<Customer_Email>metus.eu.erat@yahoo.ca</Customer_Email>
		<Customer_Phone>(392) 343-4770</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-15</last_update>
	</record>
	<record>
		<Customer_PK>851</Customer_PK>
		<Customer_ID>902</Customer_ID>
		<Customer_Name>Graiden Sims</Customer_Name>
		<Customer_Email>hendrerit.id@protonmail.org</Customer_Email>
		<Customer_Phone>1-894-547-6693</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-16</last_update>
	</record>
	<record>
		<Customer_PK>852</Customer_PK>
		<Customer_ID>667</Customer_ID>
		<Customer_Name>Arden Moss</Customer_Name>
		<Customer_Email>sapien.molestie.orci@protonmail.couk</Customer_Email>
		<Customer_Phone>1-358-568-8567</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-4-17</last_update>
	</record>
	<record>
		<Customer_PK>853</Customer_PK>
		<Customer_ID>899</Customer_ID>
		<Customer_Name>Dexter Ruiz</Customer_Name>
		<Customer_Email>nunc@hotmail.com</Customer_Email>
		<Customer_Phone>(275) 422-8559</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-4-18</last_update>
	</record>
	<record>
		<Customer_PK>854</Customer_PK>
		<Customer_ID>732</Customer_ID>
		<Customer_Name>Joelle Dudley</Customer_Name>
		<Customer_Email>dolor.fusce@google.net</Customer_Email>
		<Customer_Phone>(106) 255-2178</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-27</last_update>
	</record>
	<record>
		<Customer_PK>855</Customer_PK>
		<Customer_ID>921</Customer_ID>
		<Customer_Name>Fallon Norris</Customer_Name>
		<Customer_Email>tempus.lorem@google.ca</Customer_Email>
		<Customer_Phone>1-413-516-5648</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-13</last_update>
	</record>
	<record>
		<Customer_PK>856</Customer_PK>
		<Customer_ID>999</Customer_ID>
		<Customer_Name>Brennan Craig</Customer_Name>
		<Customer_Email>nulla@yahoo.couk</Customer_Email>
		<Customer_Phone>(671) 922-8763</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-16</last_update>
	</record>
	<record>
		<Customer_PK>857</Customer_PK>
		<Customer_ID>605</Customer_ID>
		<Customer_Name>Caryn Meyers</Customer_Name>
		<Customer_Email>quisque@outlook.couk</Customer_Email>
		<Customer_Phone>1-401-145-2727</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-1</last_update>
	</record>
	<record>
		<Customer_PK>858</Customer_PK>
		<Customer_ID>601</Customer_ID>
		<Customer_Name>Duncan Mendoza</Customer_Name>
		<Customer_Email>nec.cursus@aol.com</Customer_Email>
		<Customer_Phone>1-699-288-6767</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-8-15</last_update>
	</record>
	<record>
		<Customer_PK>859</Customer_PK>
		<Customer_ID>983</Customer_ID>
		<Customer_Name>Germaine Dillard</Customer_Name>
		<Customer_Email>fringilla.cursus.purus@google.couk</Customer_Email>
		<Customer_Phone>1-512-416-7236</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-30</last_update>
	</record>
	<record>
		<Customer_PK>860</Customer_PK>
		<Customer_ID>922</Customer_ID>
		<Customer_Name>Zachery Stafford</Customer_Name>
		<Customer_Email>a.tortor@outlook.net</Customer_Email>
		<Customer_Phone>1-666-912-8371</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-22</last_update>
	</record>
	<record>
		<Customer_PK>861</Customer_PK>
		<Customer_ID>893</Customer_ID>
		<Customer_Name>Noel Waller</Customer_Name>
		<Customer_Email>egestas.a.dui@outlook.com</Customer_Email>
		<Customer_Phone>1-556-286-7025</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-9-25</last_update>
	</record>
	<record>
		<Customer_PK>862</Customer_PK>
		<Customer_ID>676</Customer_ID>
		<Customer_Name>Sigourney Vargas</Customer_Name>
		<Customer_Email>malesuada.vel@google.edu</Customer_Email>
		<Customer_Phone>(575) 262-5346</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-5</last_update>
	</record>
	<record>
		<Customer_PK>863</Customer_PK>
		<Customer_ID>892</Customer_ID>
		<Customer_Name>Ulla Craft</Customer_Name>
		<Customer_Email>ac@aol.ca</Customer_Email>
		<Customer_Phone>1-355-381-2505</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-21</last_update>
	</record>
	<record>
		<Customer_PK>864</Customer_PK>
		<Customer_ID>827</Customer_ID>
		<Customer_Name>Nola Prince</Customer_Name>
		<Customer_Email>a.enim@hotmail.edu</Customer_Email>
		<Customer_Phone>1-616-728-1581</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-10-26</last_update>
	</record>
	<record>
		<Customer_PK>865</Customer_PK>
		<Customer_ID>979</Customer_ID>
		<Customer_Name>Oliver Ferguson</Customer_Name>
		<Customer_Email>id.ante@icloud.com</Customer_Email>
		<Customer_Phone>(254) 258-8928</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-9-13</last_update>
	</record>
	<record>
		<Customer_PK>866</Customer_PK>
		<Customer_ID>795</Customer_ID>
		<Customer_Name>Lunea Savage</Customer_Name>
		<Customer_Email>nullam.suscipit@icloud.couk</Customer_Email>
		<Customer_Phone>(376) 492-9358</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-24</last_update>
	</record>
	<record>
		<Customer_PK>867</Customer_PK>
		<Customer_ID>692</Customer_ID>
		<Customer_Name>Autumn Smith</Customer_Name>
		<Customer_Email>maecenas@yahoo.couk</Customer_Email>
		<Customer_Phone>1-470-435-8603</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-4</last_update>
	</record>
	<record>
		<Customer_PK>868</Customer_PK>
		<Customer_ID>915</Customer_ID>
		<Customer_Name>Colton Best</Customer_Name>
		<Customer_Email>risus.morbi@google.couk</Customer_Email>
		<Customer_Phone>1-306-524-6414</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-11-14</last_update>
	</record>
	<record>
		<Customer_PK>869</Customer_PK>
		<Customer_ID>917</Customer_ID>
		<Customer_Name>Owen Slater</Customer_Name>
		<Customer_Email>donec.egestas@icloud.net</Customer_Email>
		<Customer_Phone>(747) 577-2537</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-7</last_update>
	</record>
	<record>
		<Customer_PK>870</Customer_PK>
		<Customer_ID>671</Customer_ID>
		<Customer_Name>Denise Campbell</Customer_Name>
		<Customer_Email>tortor.integer@protonmail.edu</Customer_Email>
		<Customer_Phone>1-813-288-9042</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-1</last_update>
	</record>
	<record>
		<Customer_PK>871</Customer_PK>
		<Customer_ID>584</Customer_ID>
		<Customer_Name>Calista Hooper</Customer_Name>
		<Customer_Email>nullam.lobortis@icloud.net</Customer_Email>
		<Customer_Phone>1-414-953-6328</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-1-30</last_update>
	</record>
	<record>
		<Customer_PK>872</Customer_PK>
		<Customer_ID>666</Customer_ID>
		<Customer_Name>Kieran Barlow</Customer_Name>
		<Customer_Email>sem.elit@yahoo.com</Customer_Email>
		<Customer_Phone>1-716-422-6827</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-20</last_update>
	</record>
	<record>
		<Customer_PK>873</Customer_PK>
		<Customer_ID>786</Customer_ID>
		<Customer_Name>Amanda Munoz</Customer_Name>
		<Customer_Email>a.feugiat.tellus@protonmail.edu</Customer_Email>
		<Customer_Phone>1-320-372-5018</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-20</last_update>
	</record>
	<record>
		<Customer_PK>874</Customer_PK>
		<Customer_ID>925</Customer_ID>
		<Customer_Name>Howard Holden</Customer_Name>
		<Customer_Email>at@protonmail.ca</Customer_Email>
		<Customer_Phone>(933) 536-4954</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-10-23</last_update>
	</record>
	<record>
		<Customer_PK>875</Customer_PK>
		<Customer_ID>960</Customer_ID>
		<Customer_Name>Sacha Valdez</Customer_Name>
		<Customer_Email>et@hotmail.net</Customer_Email>
		<Customer_Phone>(987) 696-3153</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-1-9</last_update>
	</record>
	<record>
		<Customer_PK>876</Customer_PK>
		<Customer_ID>610</Customer_ID>
		<Customer_Name>Hamish Chapman</Customer_Name>
		<Customer_Email>malesuada.fringilla@aol.ca</Customer_Email>
		<Customer_Phone>1-224-499-6592</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-24</last_update>
	</record>
	<record>
		<Customer_PK>877</Customer_PK>
		<Customer_ID>667</Customer_ID>
		<Customer_Name>Hoyt Mccall</Customer_Name>
		<Customer_Email>et.commodo.at@google.org</Customer_Email>
		<Customer_Phone>(781) 350-1405</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-12</last_update>
	</record>
	<record>
		<Customer_PK>878</Customer_PK>
		<Customer_ID>702</Customer_ID>
		<Customer_Name>Janna Ryan</Customer_Name>
		<Customer_Email>ac.orci@google.ca</Customer_Email>
		<Customer_Phone>(742) 692-1723</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-8-3</last_update>
	</record>
	<record>
		<Customer_PK>879</Customer_PK>
		<Customer_ID>870</Customer_ID>
		<Customer_Name>Allegra Potts</Customer_Name>
		<Customer_Email>et@protonmail.edu</Customer_Email>
		<Customer_Phone>1-256-315-2866</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-14</last_update>
	</record>
	<record>
		<Customer_PK>880</Customer_PK>
		<Customer_ID>738</Customer_ID>
		<Customer_Name>Guy Rush</Customer_Name>
		<Customer_Email>tempus.risus@yahoo.net</Customer_Email>
		<Customer_Phone>1-897-654-5508</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-5</last_update>
	</record>
	<record>
		<Customer_PK>881</Customer_PK>
		<Customer_ID>840</Customer_ID>
		<Customer_Name>MacKenzie Peters</Customer_Name>
		<Customer_Email>duis@protonmail.com</Customer_Email>
		<Customer_Phone>(305) 456-9561</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-10-16</last_update>
	</record>
	<record>
		<Customer_PK>882</Customer_PK>
		<Customer_ID>753</Customer_ID>
		<Customer_Name>Azalia Johns</Customer_Name>
		<Customer_Email>scelerisque.sed@aol.org</Customer_Email>
		<Customer_Phone>(317) 698-0053</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-29</last_update>
	</record>
	<record>
		<Customer_PK>883</Customer_PK>
		<Customer_ID>890</Customer_ID>
		<Customer_Name>Charde Booker</Customer_Name>
		<Customer_Email>nec.tempus.scelerisque@yahoo.org</Customer_Email>
		<Customer_Phone>(765) 932-5468</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-4-19</last_update>
	</record>
	<record>
		<Customer_PK>884</Customer_PK>
		<Customer_ID>535</Customer_ID>
		<Customer_Name>Griffin Bright</Customer_Name>
		<Customer_Email>dapibus.ligula@icloud.net</Customer_Email>
		<Customer_Phone>1-223-767-4346</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-2</last_update>
	</record>
	<record>
		<Customer_PK>885</Customer_PK>
		<Customer_ID>713</Customer_ID>
		<Customer_Name>Uriel Ewing</Customer_Name>
		<Customer_Email>ad.litora.torquent@hotmail.couk</Customer_Email>
		<Customer_Phone>1-239-667-9416</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-10-23</last_update>
	</record>
	<record>
		<Customer_PK>886</Customer_PK>
		<Customer_ID>923</Customer_ID>
		<Customer_Name>Claire Franco</Customer_Name>
		<Customer_Email>elit.sed@icloud.couk</Customer_Email>
		<Customer_Phone>(687) 665-2657</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-11</last_update>
	</record>
	<record>
		<Customer_PK>887</Customer_PK>
		<Customer_ID>890</Customer_ID>
		<Customer_Name>Eric Hogan</Customer_Name>
		<Customer_Email>sed.nulla@hotmail.edu</Customer_Email>
		<Customer_Phone>1-486-783-7437</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-27</last_update>
	</record>
	<record>
		<Customer_PK>888</Customer_PK>
		<Customer_ID>874</Customer_ID>
		<Customer_Name>Jason Randall</Customer_Name>
		<Customer_Email>nulla.semper@outlook.ca</Customer_Email>
		<Customer_Phone>1-517-751-9814</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-8</last_update>
	</record>
	<record>
		<Customer_PK>889</Customer_PK>
		<Customer_ID>634</Customer_ID>
		<Customer_Name>Emily Nguyen</Customer_Name>
		<Customer_Email>donec.egestas@hotmail.edu</Customer_Email>
		<Customer_Phone>(886) 831-4944</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-1-24</last_update>
	</record>
	<record>
		<Customer_PK>890</Customer_PK>
		<Customer_ID>704</Customer_ID>
		<Customer_Name>Rhoda Mathews</Customer_Name>
		<Customer_Email>cursus@aol.org</Customer_Email>
		<Customer_Phone>1-220-726-5137</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-1</last_update>
	</record>
	<record>
		<Customer_PK>891</Customer_PK>
		<Customer_ID>984</Customer_ID>
		<Customer_Name>Michelle Burns</Customer_Name>
		<Customer_Email>habitant.morbi@hotmail.org</Customer_Email>
		<Customer_Phone>(743) 793-4147</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-12</last_update>
	</record>
	<record>
		<Customer_PK>892</Customer_PK>
		<Customer_ID>614</Customer_ID>
		<Customer_Name>Lacy Mullins</Customer_Name>
		<Customer_Email>tempus.scelerisque.lorem@outlook.net</Customer_Email>
		<Customer_Phone>1-666-214-7811</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-11-15</last_update>
	</record>
	<record>
		<Customer_PK>893</Customer_PK>
		<Customer_ID>555</Customer_ID>
		<Customer_Name>Ferris Carroll</Customer_Name>
		<Customer_Email>posuere@icloud.net</Customer_Email>
		<Customer_Phone>(559) 285-4831</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-15</last_update>
	</record>
	<record>
		<Customer_PK>894</Customer_PK>
		<Customer_ID>731</Customer_ID>
		<Customer_Name>Jolene Compton</Customer_Name>
		<Customer_Email>sollicitudin.commodo.ipsum@yahoo.ca</Customer_Email>
		<Customer_Phone>(578) 566-3476</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-23</last_update>
	</record>
	<record>
		<Customer_PK>895</Customer_PK>
		<Customer_ID>612</Customer_ID>
		<Customer_Name>Mallory Huff</Customer_Name>
		<Customer_Email>interdum.feugiat@aol.ca</Customer_Email>
		<Customer_Phone>(867) 501-6155</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-4-9</last_update>
	</record>
	<record>
		<Customer_PK>896</Customer_PK>
		<Customer_ID>759</Customer_ID>
		<Customer_Name>Demetrius Pate</Customer_Name>
		<Customer_Email>eu@yahoo.org</Customer_Email>
		<Customer_Phone>1-826-538-4106</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-5-16</last_update>
	</record>
	<record>
		<Customer_PK>897</Customer_PK>
		<Customer_ID>685</Customer_ID>
		<Customer_Name>Eric Becker</Customer_Name>
		<Customer_Email>elit.elit.fermentum@aol.net</Customer_Email>
		<Customer_Phone>(227) 393-6560</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-16</last_update>
	</record>
	<record>
		<Customer_PK>898</Customer_PK>
		<Customer_ID>861</Customer_ID>
		<Customer_Name>Camilla Mccarthy</Customer_Name>
		<Customer_Email>felis.orci@icloud.edu</Customer_Email>
		<Customer_Phone>1-778-785-1791</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-25</last_update>
	</record>
	<record>
		<Customer_PK>899</Customer_PK>
		<Customer_ID>849</Customer_ID>
		<Customer_Name>Perry Coffey</Customer_Name>
		<Customer_Email>lacus.pede@google.net</Customer_Email>
		<Customer_Phone>1-353-867-2888</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-22</last_update>
	</record>
	<record>
		<Customer_PK>900</Customer_PK>
		<Customer_ID>819</Customer_ID>
		<Customer_Name>Brynne Mcgee</Customer_Name>
		<Customer_Email>orci.phasellus@yahoo.org</Customer_Email>
		<Customer_Phone>1-700-687-0918</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-12</last_update>
	</record>
	<record>
		<Customer_PK>901</Customer_PK>
		<Customer_ID>710</Customer_ID>
		<Customer_Name>Vance Mejia</Customer_Name>
		<Customer_Email>cras.vulputate@outlook.net</Customer_Email>
		<Customer_Phone>1-447-871-8428</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-6</last_update>
	</record>
	<record>
		<Customer_PK>902</Customer_PK>
		<Customer_ID>550</Customer_ID>
		<Customer_Name>Rooney Mcdonald</Customer_Name>
		<Customer_Email>fusce.aliquam@yahoo.net</Customer_Email>
		<Customer_Phone>(942) 632-6765</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-2-28</last_update>
	</record>
	<record>
		<Customer_PK>903</Customer_PK>
		<Customer_ID>724</Customer_ID>
		<Customer_Name>Lance Whitehead</Customer_Name>
		<Customer_Email>mauris.sagittis.placerat@google.couk</Customer_Email>
		<Customer_Phone>1-311-434-6428</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-1</last_update>
	</record>
	<record>
		<Customer_PK>904</Customer_PK>
		<Customer_ID>887</Customer_ID>
		<Customer_Name>Fitzgerald Joyce</Customer_Name>
		<Customer_Email>nec.leo.morbi@outlook.edu</Customer_Email>
		<Customer_Phone>(464) 687-2446</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-11-2</last_update>
	</record>
	<record>
		<Customer_PK>905</Customer_PK>
		<Customer_ID>901</Customer_ID>
		<Customer_Name>Dieter Sandoval</Customer_Name>
		<Customer_Email>nullam.lobortis@protonmail.net</Customer_Email>
		<Customer_Phone>(824) 261-6125</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-15</last_update>
	</record>
	<record>
		<Customer_PK>906</Customer_PK>
		<Customer_ID>989</Customer_ID>
		<Customer_Name>Rose Estes</Customer_Name>
		<Customer_Email>faucibus@outlook.ca</Customer_Email>
		<Customer_Phone>1-907-478-1343</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-27</last_update>
	</record>
	<record>
		<Customer_PK>907</Customer_PK>
		<Customer_ID>914</Customer_ID>
		<Customer_Name>Caleb O'donnell</Customer_Name>
		<Customer_Email>consequat@outlook.couk</Customer_Email>
		<Customer_Phone>(572) 514-5224</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-5</last_update>
	</record>
	<record>
		<Customer_PK>908</Customer_PK>
		<Customer_ID>968</Customer_ID>
		<Customer_Name>Meredith Reese</Customer_Name>
		<Customer_Email>vitae.orci@icloud.edu</Customer_Email>
		<Customer_Phone>(355) 990-7776</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-28</last_update>
	</record>
	<record>
		<Customer_PK>909</Customer_PK>
		<Customer_ID>652</Customer_ID>
		<Customer_Name>Inez Forbes</Customer_Name>
		<Customer_Email>cubilia.curae@aol.edu</Customer_Email>
		<Customer_Phone>(743) 881-0237</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-19</last_update>
	</record>
	<record>
		<Customer_PK>910</Customer_PK>
		<Customer_ID>969</Customer_ID>
		<Customer_Name>Wang Kennedy</Customer_Name>
		<Customer_Email>ut.sem@aol.couk</Customer_Email>
		<Customer_Phone>1-815-236-7195</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-27</last_update>
	</record>
	<record>
		<Customer_PK>911</Customer_PK>
		<Customer_ID>568</Customer_ID>
		<Customer_Name>Joan Keith</Customer_Name>
		<Customer_Email>at@protonmail.edu</Customer_Email>
		<Customer_Phone>1-154-843-2640</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-13</last_update>
	</record>
	<record>
		<Customer_PK>912</Customer_PK>
		<Customer_ID>987</Customer_ID>
		<Customer_Name>Driscoll Dominguez</Customer_Name>
		<Customer_Email>eros.non.enim@aol.couk</Customer_Email>
		<Customer_Phone>1-877-753-8640</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-4-27</last_update>
	</record>
	<record>
		<Customer_PK>913</Customer_PK>
		<Customer_ID>953</Customer_ID>
		<Customer_Name>Marshall Wall</Customer_Name>
		<Customer_Email>fusce.dolor.quam@hotmail.couk</Customer_Email>
		<Customer_Phone>1-718-686-6499</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-15</last_update>
	</record>
	<record>
		<Customer_PK>914</Customer_PK>
		<Customer_ID>555</Customer_ID>
		<Customer_Name>Roth Holland</Customer_Name>
		<Customer_Email>interdum@google.com</Customer_Email>
		<Customer_Phone>1-620-543-1104</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-12</last_update>
	</record>
	<record>
		<Customer_PK>915</Customer_PK>
		<Customer_ID>856</Customer_ID>
		<Customer_Name>Ciaran Rodriquez</Customer_Name>
		<Customer_Email>ligula.donec@yahoo.edu</Customer_Email>
		<Customer_Phone>1-952-877-0775</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-2-27</last_update>
	</record>
	<record>
		<Customer_PK>916</Customer_PK>
		<Customer_ID>908</Customer_ID>
		<Customer_Name>Joan Rollins</Customer_Name>
		<Customer_Email>nisi.mauris@icloud.net</Customer_Email>
		<Customer_Phone>(736) 728-4218</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-4-16</last_update>
	</record>
	<record>
		<Customer_PK>917</Customer_PK>
		<Customer_ID>989</Customer_ID>
		<Customer_Name>Lesley Mcintosh</Customer_Name>
		<Customer_Email>vehicula@aol.net</Customer_Email>
		<Customer_Phone>(435) 182-4043</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-7-26</last_update>
	</record>
	<record>
		<Customer_PK>918</Customer_PK>
		<Customer_ID>875</Customer_ID>
		<Customer_Name>Indira Estrada</Customer_Name>
		<Customer_Email>rutrum.lorem@protonmail.org</Customer_Email>
		<Customer_Phone>1-546-957-6672</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-10-21</last_update>
	</record>
	<record>
		<Customer_PK>919</Customer_PK>
		<Customer_ID>635</Customer_ID>
		<Customer_Name>Gail Moore</Customer_Name>
		<Customer_Email>consequat.auctor.nunc@hotmail.com</Customer_Email>
		<Customer_Phone>1-599-551-8413</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-29</last_update>
	</record>
	<record>
		<Customer_PK>920</Customer_PK>
		<Customer_ID>666</Customer_ID>
		<Customer_Name>Jarrod Burks</Customer_Name>
		<Customer_Email>sed.nunc.est@protonmail.com</Customer_Email>
		<Customer_Phone>(544) 377-2182</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-27</last_update>
	</record>
	<record>
		<Customer_PK>921</Customer_PK>
		<Customer_ID>719</Customer_ID>
		<Customer_Name>Tyler Walls</Customer_Name>
		<Customer_Email>iaculis.lacus.pede@hotmail.com</Customer_Email>
		<Customer_Phone>(580) 473-8241</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-4-26</last_update>
	</record>
	<record>
		<Customer_PK>922</Customer_PK>
		<Customer_ID>811</Customer_ID>
		<Customer_Name>Madonna Tillman</Customer_Name>
		<Customer_Email>gravida.molestie.arcu@google.org</Customer_Email>
		<Customer_Phone>(868) 973-4266</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-15</last_update>
	</record>
	<record>
		<Customer_PK>923</Customer_PK>
		<Customer_ID>540</Customer_ID>
		<Customer_Name>Austin Perry</Customer_Name>
		<Customer_Email>venenatis.vel@outlook.com</Customer_Email>
		<Customer_Phone>(154) 697-1432</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-17</last_update>
	</record>
	<record>
		<Customer_PK>924</Customer_PK>
		<Customer_ID>598</Customer_ID>
		<Customer_Name>Karly Turner</Customer_Name>
		<Customer_Email>non.enim.commodo@outlook.org</Customer_Email>
		<Customer_Phone>1-560-310-1567</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-6</last_update>
	</record>
	<record>
		<Customer_PK>925</Customer_PK>
		<Customer_ID>977</Customer_ID>
		<Customer_Name>Wendy Aguilar</Customer_Name>
		<Customer_Email>mauris.magna@icloud.com</Customer_Email>
		<Customer_Phone>1-327-757-4818</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-26</last_update>
	</record>
	<record>
		<Customer_PK>926</Customer_PK>
		<Customer_ID>873</Customer_ID>
		<Customer_Name>Alvin Klein</Customer_Name>
		<Customer_Email>nunc.quis.arcu@aol.edu</Customer_Email>
		<Customer_Phone>1-962-335-6928</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-4</last_update>
	</record>
	<record>
		<Customer_PK>927</Customer_PK>
		<Customer_ID>564</Customer_ID>
		<Customer_Name>Jin Adkins</Customer_Name>
		<Customer_Email>orci@icloud.ca</Customer_Email>
		<Customer_Phone>1-284-843-8608</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-4-1</last_update>
	</record>
	<record>
		<Customer_PK>928</Customer_PK>
		<Customer_ID>616</Customer_ID>
		<Customer_Name>Audrey Alexander</Customer_Name>
		<Customer_Email>magna.sed.eu@outlook.com</Customer_Email>
		<Customer_Phone>(228) 216-3654</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-17</last_update>
	</record>
	<record>
		<Customer_PK>929</Customer_PK>
		<Customer_ID>592</Customer_ID>
		<Customer_Name>Caleb Hays</Customer_Name>
		<Customer_Email>luctus.lobortis.class@protonmail.couk</Customer_Email>
		<Customer_Phone>(534) 211-3538</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-4-4</last_update>
	</record>
	<record>
		<Customer_PK>930</Customer_PK>
		<Customer_ID>842</Customer_ID>
		<Customer_Name>Hanae Waters</Customer_Name>
		<Customer_Email>orci.luctus@protonmail.couk</Customer_Email>
		<Customer_Phone>1-337-786-4291</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-26</last_update>
	</record>
	<record>
		<Customer_PK>931</Customer_PK>
		<Customer_ID>903</Customer_ID>
		<Customer_Name>Martena Guerrero</Customer_Name>
		<Customer_Email>molestie@aol.com</Customer_Email>
		<Customer_Phone>(669) 782-0277</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-27</last_update>
	</record>
	<record>
		<Customer_PK>932</Customer_PK>
		<Customer_ID>984</Customer_ID>
		<Customer_Name>Lysandra Kemp</Customer_Name>
		<Customer_Email>quisque@google.couk</Customer_Email>
		<Customer_Phone>1-634-538-5448</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-9</last_update>
	</record>
	<record>
		<Customer_PK>933</Customer_PK>
		<Customer_ID>603</Customer_ID>
		<Customer_Name>Damian Hines</Customer_Name>
		<Customer_Email>justo.sit@yahoo.org</Customer_Email>
		<Customer_Phone>1-356-218-8646</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-25</last_update>
	</record>
	<record>
		<Customer_PK>934</Customer_PK>
		<Customer_ID>618</Customer_ID>
		<Customer_Name>Ora Atkinson</Customer_Name>
		<Customer_Email>ipsum.primis.in@google.edu</Customer_Email>
		<Customer_Phone>(515) 447-6263</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-17</last_update>
	</record>
	<record>
		<Customer_PK>935</Customer_PK>
		<Customer_ID>832</Customer_ID>
		<Customer_Name>Barclay Britt</Customer_Name>
		<Customer_Email>mollis.vitae@protonmail.couk</Customer_Email>
		<Customer_Phone>(180) 988-2657</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-21</last_update>
	</record>
	<record>
		<Customer_PK>936</Customer_PK>
		<Customer_ID>680</Customer_ID>
		<Customer_Name>Neville Moss</Customer_Name>
		<Customer_Email>ridiculus.mus@yahoo.net</Customer_Email>
		<Customer_Phone>1-363-628-2512</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-29</last_update>
	</record>
	<record>
		<Customer_PK>937</Customer_PK>
		<Customer_ID>731</Customer_ID>
		<Customer_Name>Paloma Wynn</Customer_Name>
		<Customer_Email>in.scelerisque@hotmail.ca</Customer_Email>
		<Customer_Phone>(713) 244-5256</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-7-9</last_update>
	</record>
	<record>
		<Customer_PK>938</Customer_PK>
		<Customer_ID>695</Customer_ID>
		<Customer_Name>Wade Rodgers</Customer_Name>
		<Customer_Email>cras.pellentesque.sed@protonmail.ca</Customer_Email>
		<Customer_Phone>(132) 783-1100</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-15</last_update>
	</record>
	<record>
		<Customer_PK>939</Customer_PK>
		<Customer_ID>695</Customer_ID>
		<Customer_Name>Quail Mccarty</Customer_Name>
		<Customer_Email>aliquam.vulputate@hotmail.com</Customer_Email>
		<Customer_Phone>1-895-371-4845</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-7</last_update>
	</record>
	<record>
		<Customer_PK>940</Customer_PK>
		<Customer_ID>839</Customer_ID>
		<Customer_Name>Alice Dawson</Customer_Name>
		<Customer_Email>arcu@yahoo.ca</Customer_Email>
		<Customer_Phone>(772) 719-3225</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-29</last_update>
	</record>
	<record>
		<Customer_PK>941</Customer_PK>
		<Customer_ID>838</Customer_ID>
		<Customer_Name>Tiger Brennan</Customer_Name>
		<Customer_Email>suspendisse.sed.dolor@yahoo.edu</Customer_Email>
		<Customer_Phone>1-839-780-3672</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-28</last_update>
	</record>
	<record>
		<Customer_PK>942</Customer_PK>
		<Customer_ID>923</Customer_ID>
		<Customer_Name>Neville Bartlett</Customer_Name>
		<Customer_Email>venenatis.lacus.etiam@hotmail.com</Customer_Email>
		<Customer_Phone>(780) 886-2416</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-8-31</last_update>
	</record>
	<record>
		<Customer_PK>943</Customer_PK>
		<Customer_ID>968</Customer_ID>
		<Customer_Name>Ingrid Kemp</Customer_Name>
		<Customer_Email>tincidunt@aol.org</Customer_Email>
		<Customer_Phone>1-951-725-2692</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-6</last_update>
	</record>
	<record>
		<Customer_PK>944</Customer_PK>
		<Customer_ID>642</Customer_ID>
		<Customer_Name>Uta Woodard</Customer_Name>
		<Customer_Email>lacinia.vitae@outlook.edu</Customer_Email>
		<Customer_Phone>1-355-732-9524</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-6</last_update>
	</record>
	<record>
		<Customer_PK>945</Customer_PK>
		<Customer_ID>946</Customer_ID>
		<Customer_Name>Audra Ellison</Customer_Name>
		<Customer_Email>urna.ut@hotmail.com</Customer_Email>
		<Customer_Phone>(696) 882-2435</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-4</last_update>
	</record>
	<record>
		<Customer_PK>946</Customer_PK>
		<Customer_ID>963</Customer_ID>
		<Customer_Name>Ross Ballard</Customer_Name>
		<Customer_Email>ut.eros.non@hotmail.ca</Customer_Email>
		<Customer_Phone>(631) 546-5950</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-20</last_update>
	</record>
	<record>
		<Customer_PK>947</Customer_PK>
		<Customer_ID>816</Customer_ID>
		<Customer_Name>Kaseem Calderon</Customer_Name>
		<Customer_Email>lectus@outlook.org</Customer_Email>
		<Customer_Phone>(390) 778-7891</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-9-19</last_update>
	</record>
	<record>
		<Customer_PK>948</Customer_PK>
		<Customer_ID>593</Customer_ID>
		<Customer_Name>Eaton Dotson</Customer_Name>
		<Customer_Email>eu.metus@google.couk</Customer_Email>
		<Customer_Phone>(411) 474-5561</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-4</last_update>
	</record>
	<record>
		<Customer_PK>949</Customer_PK>
		<Customer_ID>585</Customer_ID>
		<Customer_Name>Tanisha Lester</Customer_Name>
		<Customer_Email>amet.ante@aol.org</Customer_Email>
		<Customer_Phone>1-730-303-3208</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-4</last_update>
	</record>
	<record>
		<Customer_PK>950</Customer_PK>
		<Customer_ID>813</Customer_ID>
		<Customer_Name>Macaulay Avery</Customer_Name>
		<Customer_Email>mauris.molestie.pharetra@hotmail.couk</Customer_Email>
		<Customer_Phone>(537) 860-1115</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-28</last_update>
	</record>
	<record>
		<Customer_PK>951</Customer_PK>
		<Customer_ID>642</Customer_ID>
		<Customer_Name>Gillian Brennan</Customer_Name>
		<Customer_Email>nunc@outlook.com</Customer_Email>
		<Customer_Phone>(552) 549-0888</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-5</last_update>
	</record>
	<record>
		<Customer_PK>952</Customer_PK>
		<Customer_ID>638</Customer_ID>
		<Customer_Name>Velma Roth</Customer_Name>
		<Customer_Email>curae.phasellus@google.couk</Customer_Email>
		<Customer_Phone>1-564-232-4873</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-1-14</last_update>
	</record>
	<record>
		<Customer_PK>953</Customer_PK>
		<Customer_ID>510</Customer_ID>
		<Customer_Name>Damon Bishop</Customer_Name>
		<Customer_Email>conubia@outlook.org</Customer_Email>
		<Customer_Phone>(637) 936-3482</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-8-27</last_update>
	</record>
	<record>
		<Customer_PK>954</Customer_PK>
		<Customer_ID>915</Customer_ID>
		<Customer_Name>Marshall David</Customer_Name>
		<Customer_Email>lorem.ipsum.dolor@hotmail.couk</Customer_Email>
		<Customer_Phone>(386) 956-3684</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-10-25</last_update>
	</record>
	<record>
		<Customer_PK>955</Customer_PK>
		<Customer_ID>830</Customer_ID>
		<Customer_Name>Gillian Pruitt</Customer_Name>
		<Customer_Email>mollis.vitae@google.couk</Customer_Email>
		<Customer_Phone>1-363-592-6062</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-11</last_update>
	</record>
	<record>
		<Customer_PK>956</Customer_PK>
		<Customer_ID>542</Customer_ID>
		<Customer_Name>Kenneth Graves</Customer_Name>
		<Customer_Email>vivamus.euismod.urna@aol.couk</Customer_Email>
		<Customer_Phone>1-744-627-1024</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-10</last_update>
	</record>
	<record>
		<Customer_PK>957</Customer_PK>
		<Customer_ID>510</Customer_ID>
		<Customer_Name>Quin Wood</Customer_Name>
		<Customer_Email>dolor@protonmail.com</Customer_Email>
		<Customer_Phone>(386) 762-3646</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-23</last_update>
	</record>
	<record>
		<Customer_PK>958</Customer_PK>
		<Customer_ID>894</Customer_ID>
		<Customer_Name>Ryder Forbes</Customer_Name>
		<Customer_Email>amet.ante@hotmail.couk</Customer_Email>
		<Customer_Phone>1-753-773-5746</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-10-21</last_update>
	</record>
	<record>
		<Customer_PK>959</Customer_PK>
		<Customer_ID>712</Customer_ID>
		<Customer_Name>Cassandra Hatfield</Customer_Name>
		<Customer_Email>ante.ipsum@hotmail.couk</Customer_Email>
		<Customer_Phone>(227) 845-1428</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-12-15</last_update>
	</record>
	<record>
		<Customer_PK>960</Customer_PK>
		<Customer_ID>876</Customer_ID>
		<Customer_Name>Finn Mercer</Customer_Name>
		<Customer_Email>non@icloud.org</Customer_Email>
		<Customer_Phone>1-673-594-3928</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-9</last_update>
	</record>
	<record>
		<Customer_PK>961</Customer_PK>
		<Customer_ID>867</Customer_ID>
		<Customer_Name>Ray Cameron</Customer_Name>
		<Customer_Email>parturient.montes.nascetur@outlook.org</Customer_Email>
		<Customer_Phone>(348) 916-7783</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-13</last_update>
	</record>
	<record>
		<Customer_PK>962</Customer_PK>
		<Customer_ID>876</Customer_ID>
		<Customer_Name>Brady James</Customer_Name>
		<Customer_Email>mi.lorem@icloud.org</Customer_Email>
		<Customer_Phone>(407) 601-1803</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-1-9</last_update>
	</record>
	<record>
		<Customer_PK>963</Customer_PK>
		<Customer_ID>629</Customer_ID>
		<Customer_Name>Lenore Puckett</Customer_Name>
		<Customer_Email>lobortis@protonmail.com</Customer_Email>
		<Customer_Phone>(181) 811-7194</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-8-18</last_update>
	</record>
	<record>
		<Customer_PK>964</Customer_PK>
		<Customer_ID>973</Customer_ID>
		<Customer_Name>Holly Jenkins</Customer_Name>
		<Customer_Email>ac.urna.ut@icloud.com</Customer_Email>
		<Customer_Phone>1-268-382-1652</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-4-18</last_update>
	</record>
	<record>
		<Customer_PK>965</Customer_PK>
		<Customer_ID>696</Customer_ID>
		<Customer_Name>Wesley Dorsey</Customer_Name>
		<Customer_Email>ante.dictum@google.ca</Customer_Email>
		<Customer_Phone>(844) 308-9605</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-17</last_update>
	</record>
	<record>
		<Customer_PK>966</Customer_PK>
		<Customer_ID>823</Customer_ID>
		<Customer_Name>Daria Carrillo</Customer_Name>
		<Customer_Email>ante@protonmail.org</Customer_Email>
		<Customer_Phone>(376) 553-0618</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-18</last_update>
	</record>
	<record>
		<Customer_PK>967</Customer_PK>
		<Customer_ID>949</Customer_ID>
		<Customer_Name>Channing Mcclain</Customer_Name>
		<Customer_Email>non.hendrerit.id@icloud.ca</Customer_Email>
		<Customer_Phone>1-434-708-3363</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-16</last_update>
	</record>
	<record>
		<Customer_PK>968</Customer_PK>
		<Customer_ID>633</Customer_ID>
		<Customer_Name>Carl Mayer</Customer_Name>
		<Customer_Email>fermentum@hotmail.org</Customer_Email>
		<Customer_Phone>(216) 217-6926</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-7-23</last_update>
	</record>
	<record>
		<Customer_PK>969</Customer_PK>
		<Customer_ID>587</Customer_ID>
		<Customer_Name>Molly Mclean</Customer_Name>
		<Customer_Email>felis@hotmail.edu</Customer_Email>
		<Customer_Phone>1-531-713-4458</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-7</last_update>
	</record>
	<record>
		<Customer_PK>970</Customer_PK>
		<Customer_ID>777</Customer_ID>
		<Customer_Name>Chiquita Hays</Customer_Name>
		<Customer_Email>lectus.sit@yahoo.org</Customer_Email>
		<Customer_Phone>(154) 481-6787</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-6-16</last_update>
	</record>
	<record>
		<Customer_PK>971</Customer_PK>
		<Customer_ID>964</Customer_ID>
		<Customer_Name>Salvador Chavez</Customer_Name>
		<Customer_Email>placerat.augue@google.ca</Customer_Email>
		<Customer_Phone>1-114-216-8666</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-4-25</last_update>
	</record>
	<record>
		<Customer_PK>972</Customer_PK>
		<Customer_ID>754</Customer_ID>
		<Customer_Name>Amal Juarez</Customer_Name>
		<Customer_Email>ultrices.sit@outlook.edu</Customer_Email>
		<Customer_Phone>1-611-555-0521</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-11-2</last_update>
	</record>
	<record>
		<Customer_PK>973</Customer_PK>
		<Customer_ID>785</Customer_ID>
		<Customer_Name>Fallon Mcgowan</Customer_Name>
		<Customer_Email>malesuada.malesuada@aol.edu</Customer_Email>
		<Customer_Phone>(428) 479-7130</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-18</last_update>
	</record>
	<record>
		<Customer_PK>974</Customer_PK>
		<Customer_ID>506</Customer_ID>
		<Customer_Name>Olga Levine</Customer_Name>
		<Customer_Email>posuere.enim@outlook.com</Customer_Email>
		<Customer_Phone>1-887-342-1845</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-10-6</last_update>
	</record>
	<record>
		<Customer_PK>975</Customer_PK>
		<Customer_ID>912</Customer_ID>
		<Customer_Name>Hoyt Buchanan</Customer_Name>
		<Customer_Email>nam.ac.nulla@yahoo.org</Customer_Email>
		<Customer_Phone>1-412-547-7534</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-10-29</last_update>
	</record>
	<record>
		<Customer_PK>976</Customer_PK>
		<Customer_ID>784</Customer_ID>
		<Customer_Name>Mariko Parker</Customer_Name>
		<Customer_Email>sit.amet.ante@hotmail.edu</Customer_Email>
		<Customer_Phone>(444) 543-8948</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-28</last_update>
	</record>
	<record>
		<Customer_PK>977</Customer_PK>
		<Customer_ID>871</Customer_ID>
		<Customer_Name>Olga Key</Customer_Name>
		<Customer_Email>malesuada.integer@protonmail.couk</Customer_Email>
		<Customer_Phone>(486) 614-8758</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-3-9</last_update>
	</record>
	<record>
		<Customer_PK>978</Customer_PK>
		<Customer_ID>532</Customer_ID>
		<Customer_Name>Yasir Bonner</Customer_Name>
		<Customer_Email>non.luctus.sit@protonmail.org</Customer_Email>
		<Customer_Phone>1-447-615-3883</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-2-28</last_update>
	</record>
	<record>
		<Customer_PK>979</Customer_PK>
		<Customer_ID>603</Customer_ID>
		<Customer_Name>Natalie Thornton</Customer_Name>
		<Customer_Email>tempus.scelerisque@aol.com</Customer_Email>
		<Customer_Phone>1-750-571-9932</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-14</last_update>
	</record>
	<record>
		<Customer_PK>980</Customer_PK>
		<Customer_ID>877</Customer_ID>
		<Customer_Name>Kellie Andrews</Customer_Name>
		<Customer_Email>eu.eros@hotmail.org</Customer_Email>
		<Customer_Phone>1-729-346-9470</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-1-25</last_update>
	</record>
	<record>
		<Customer_PK>981</Customer_PK>
		<Customer_ID>641</Customer_ID>
		<Customer_Name>Merritt Strong</Customer_Name>
		<Customer_Email>suspendisse.tristique@aol.edu</Customer_Email>
		<Customer_Phone>1-459-282-3654</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-26</last_update>
	</record>
	<record>
		<Customer_PK>982</Customer_PK>
		<Customer_ID>934</Customer_ID>
		<Customer_Name>Ferdinand Castaneda</Customer_Name>
		<Customer_Email>et.ultrices@protonmail.net</Customer_Email>
		<Customer_Phone>1-526-862-7464</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-11-26</last_update>
	</record>
	<record>
		<Customer_PK>983</Customer_PK>
		<Customer_ID>901</Customer_ID>
		<Customer_Name>Shafira Poole</Customer_Name>
		<Customer_Email>et.netus@protonmail.couk</Customer_Email>
		<Customer_Phone>1-376-279-4007</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-13</last_update>
	</record>
	<record>
		<Customer_PK>984</Customer_PK>
		<Customer_ID>869</Customer_ID>
		<Customer_Name>Perry Pena</Customer_Name>
		<Customer_Email>vel.venenatis.vel@icloud.couk</Customer_Email>
		<Customer_Phone>1-112-266-1054</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-3-18</last_update>
	</record>
	<record>
		<Customer_PK>985</Customer_PK>
		<Customer_ID>636</Customer_ID>
		<Customer_Name>Marshall Hammond</Customer_Name>
		<Customer_Email>amet@outlook.org</Customer_Email>
		<Customer_Phone>1-469-276-5102</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-12-25</last_update>
	</record>
	<record>
		<Customer_PK>986</Customer_PK>
		<Customer_ID>932</Customer_ID>
		<Customer_Name>Sheila Page</Customer_Name>
		<Customer_Email>nullam@yahoo.edu</Customer_Email>
		<Customer_Phone>(281) 443-0022</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-4-18</last_update>
	</record>
	<record>
		<Customer_PK>987</Customer_PK>
		<Customer_ID>670</Customer_ID>
		<Customer_Name>Sigourney Richmond</Customer_Name>
		<Customer_Email>malesuada@yahoo.org</Customer_Email>
		<Customer_Phone>1-835-624-2855</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-5-2</last_update>
	</record>
	<record>
		<Customer_PK>988</Customer_PK>
		<Customer_ID>639</Customer_ID>
		<Customer_Name>Walter Sexton</Customer_Name>
		<Customer_Email>consectetuer.cursus@google.ca</Customer_Email>
		<Customer_Phone>1-688-518-0587</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-6</last_update>
	</record>
	<record>
		<Customer_PK>989</Customer_PK>
		<Customer_ID>949</Customer_ID>
		<Customer_Name>Linda Berry</Customer_Name>
		<Customer_Email>elementum.purus@aol.couk</Customer_Email>
		<Customer_Phone>1-412-671-5426</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-1-23</last_update>
	</record>
	<record>
		<Customer_PK>990</Customer_PK>
		<Customer_ID>967</Customer_ID>
		<Customer_Name>Cara Baird</Customer_Name>
		<Customer_Email>dui.nec.urna@outlook.ca</Customer_Email>
		<Customer_Phone>(278) 364-0376</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-9-26</last_update>
	</record>
	<record>
		<Customer_PK>991</Customer_PK>
		<Customer_ID>835</Customer_ID>
		<Customer_Name>Yasir Lester</Customer_Name>
		<Customer_Email>sed.nunc@protonmail.net</Customer_Email>
		<Customer_Phone>1-448-426-2768</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-6-6</last_update>
	</record>
	<record>
		<Customer_PK>992</Customer_PK>
		<Customer_ID>519</Customer_ID>
		<Customer_Name>Xyla Cantu</Customer_Name>
		<Customer_Email>egestas@hotmail.net</Customer_Email>
		<Customer_Phone>(552) 962-8255</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-6-22</last_update>
	</record>
	<record>
		<Customer_PK>993</Customer_PK>
		<Customer_ID>695</Customer_ID>
		<Customer_Name>Jacob Wooten</Customer_Name>
		<Customer_Email>malesuada.ut@yahoo.com</Customer_Email>
		<Customer_Phone>(621) 784-5125</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-9-29</last_update>
	</record>
	<record>
		<Customer_PK>994</Customer_PK>
		<Customer_ID>832</Customer_ID>
		<Customer_Name>Pascale Beasley</Customer_Name>
		<Customer_Email>lorem@hotmail.org</Customer_Email>
		<Customer_Phone>1-453-353-5611</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-3-17</last_update>
	</record>
	<record>
		<Customer_PK>995</Customer_PK>
		<Customer_ID>867</Customer_ID>
		<Customer_Name>Isadora Winters</Customer_Name>
		<Customer_Email>vehicula.pellentesque@yahoo.com</Customer_Email>
		<Customer_Phone>(670) 741-2554</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-12-26</last_update>
	</record>
	<record>
		<Customer_PK>996</Customer_PK>
		<Customer_ID>559</Customer_ID>
		<Customer_Name>Simone Sloan</Customer_Name>
		<Customer_Email>aliquam.auctor@protonmail.com</Customer_Email>
		<Customer_Phone>(884) 218-5249</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-4-15</last_update>
	</record>
	<record>
		<Customer_PK>997</Customer_PK>
		<Customer_ID>659</Customer_ID>
		<Customer_Name>Galena Welch</Customer_Name>
		<Customer_Email>ac.libero.nec@yahoo.com</Customer_Email>
		<Customer_Phone>(219) 134-3677</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-9-22</last_update>
	</record>
	<record>
		<Customer_PK>998</Customer_PK>
		<Customer_ID>726</Customer_ID>
		<Customer_Name>Nichole Kirk</Customer_Name>
		<Customer_Email>in@protonmail.com</Customer_Email>
		<Customer_Phone>(869) 282-4488</Customer_Phone>
		<Customer_Segment>Empresarial </Customer_Segment>
		<last_update>2022-9-2</last_update>
	</record>
	<record>
		<Customer_PK>999</Customer_PK>
		<Customer_ID>938</Customer_ID>
		<Customer_Name>Neve Schroeder</Customer_Name>
		<Customer_Email>tempus.eu.ligula@yahoo.net</Customer_Email>
		<Customer_Phone>(451) 466-9178</Customer_Phone>
		<Customer_Segment>Joven</Customer_Segment>
		<last_update>2022-2-22</last_update>
	</record>
	<record>
		<Customer_PK>1000</Customer_PK>
		<Customer_ID>819</Customer_ID>
		<Customer_Name>Althea Carter</Customer_Name>
		<Customer_Email>amet.consectetuer@hotmail.net</Customer_Email>
		<Customer_Phone>1-969-866-2041</Customer_Phone>
		<Customer_Segment>Minorista</Customer_Segment>
		<last_update>2022-9-21</last_update>
	</record>
</records>
'''

# Parsea el XML
root = ET.fromstring(xml_data)

# Actualiza los registros según las instrucciones
for i, record in enumerate(root.findall('record')):
    segment = record.find('Customer_Segment')
    if i < 500:
        segment.text = 'Joven'
    elif 500 <= i < 800:
        segment.text = 'Minorista'
    else:
        segment.text = 'Empresarial'

# Guarda el XML actualizado en un archivo (o lo que quieras hacer con él)
tree = ET.ElementTree(root)
tree.write('updated_customers.xml')

print("XML Updated!")
