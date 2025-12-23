# Input/Output

## Overview

The Jay40 provides access to 39 of the FPGA's programmable I/O pins. These pins are exposed through the board's two 24-pin connectors and are labeled **D0** through **D38**. Each programmable I/O can be configured as an input, output, or tri-state buffer. In addition, an internal pull-up resistor can be enabled for each pin. For more detail, please refer to the "iCE40 Family Data Sheet."

The board's connectors also provide the pins required to program the FPGA and flash chip. This is done through a standard SPI interface (**CS**, **SCK**, **MOSI**, and **MISO**) and two dedicated FPGA configuration pins, **CRST** and **CDN**.

For power, the board includes several **3V3** and **GND** pins, as well as a **5V** pin. Depending on the setup, these power pins be used as either power inputs or power outputs.

## Connector Pinout

The board's pinout is shown in __. Aside from the single **5V** power pin, all of the board's I/O operate at a 3.3 V logic level.

![Alt text](diag/jay40_pinout.svg){: style="width: 30rem;"}




<table>
    <colgroup>
        <col style="width: 4rem;">
        <col style="width: 7rem;">
        <col style="width: auto; min-width: 11rem;">
        <col style="width: 4rem;">
        <col style="width: 7rem;">
        <col style="width: auto; min-width: 11rem;">
    </colgroup>
    <thead>
        <tr>
          <th>Pin</th>
          <th>Pin Name</th>
          <th>Description</th>
          <th>Pin</th>
          <th>Pin Name</th>
          <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>3V3</td>
            <td>3.3 V Power</td>
            <td>15</td>
            <td>3V3</td>
            <td>3.3 V Power</td>
        </tr>
        <tr>
            <td>2</td>
            <td>GND</td>
            <td>Ground</td>
            <td>16</td>
            <td>GND</td>
            <td>Ground</td>
        </tr>
        <tr>
            <td>3</td>
            <td>D0</td>
            <td>Programmable I/O</td>
            <td>17</td>
            <td>D8</td>
            <td>Programmable I/O</td>
        </tr>
        <tr>
            <td>4</td>
            <td>D1</td>
            <td>Programmable I/O</td>
            <td>18</td>
            <td>D9</td>
            <td>Programmable I/O</td>
        </tr>
        <tr>
            <td>5</td>
            <td>D2</td>
            <td>Programmable I/O</td>
            <td>19</td>
            <td>D10</td>
            <td>Programmable I/O</td>
        </tr>
        <tr>
            <td>6</td>
            <td>D3</td>
            <td>Programmable I/O</td>
            <td>20</td>
            <td>D11</td>
            <td>Programmable I/O</td>
        </tr>
        <tr>
            <td>7</td>
            <td>D4</td>
            <td>Programmable I/O</td>
            <td>21</td>
            <td>D12</td>
            <td>Programmable I/O</td>
        </tr>
        <tr>
            <td>8</td>
            <td>D5</td>
            <td>Programmable I/O</td>
            <td>22</td>
            <td>D13</td>
            <td>Programmable I/O</td>
        </tr>
        <tr>
            <td>9</td>
            <td>D6</td>
            <td>Programmable I/O</td>
            <td>23</td>
            <td>D14</td>
            <td>Programmable I/O</td>
        </tr>
        <tr>
            <td>10</td>
            <td>D7</td>
            <td>Programmable I/O</td>
            <td>24</td>
            <td>D15</td>
            <td>Programmable I/O</td>
        </tr>
        <tr>
            <td>11</td>
            <td>MOSI</td>
            <td>SPI Master Out Slave In</td>
            <td>25</td>
            <td>CS</td>
            <td>SPI Chip Select</td>
        </tr>
        <tr>
            <td>12</td>
            <td>MISO</td>
            <td>SPI Master In Slave Out</td>
            <td>26</td>
            <td>SCK</td>
            <td>SPI Serial Clock</td>
        </tr>
        <tr>
            <td>13</td>
            <td>GND</td>
            <td>Ground</td>
            <td>27</td>
            <td>CDN</td>
            <td>Configuration Done</td>
        </tr>
        <tr>
            <td>14</td>
            <td>3V3</td>
            <td>3.3 V Power</td>
            <td>28</td>
            <td>CRST</td>
            <td>Configuration Reset</td>
        </tr>
    </tbody>
</table>

<table>
    <colgroup>
        <col style="width: 4rem;">
        <col style="width: 7rem;">
        <col style="width: auto; min-width: 11rem;">
        <col style="width: 4rem;">
        <col style="width: 7rem;">
        <col style="width: auto; min-width: 11rem;">
    </colgroup>
    <thead>
        <tr>
            <th>Pin</th>
            <th>Pin Name</th>
            <th>Description</th>
            <th>Pin</th>
            <th>Pin Name</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>D16</td>
            <td>Programmable I/O</td>
            <td>15</td>
            <td>5V</td>
            <td>5 V Power</td>
        </tr>
        <tr>
            <td>2</td>
            <td>D17</td>
            <td>Programmable I/O</td>
            <td>16</td>
            <td>D28</td>
            <td>Programmable I/O</td>
        </tr>
        <tr>
            <td>3</td>
            <td>D18</td>
            <td>Programmable I/O</td>
            <td>17</td>
            <td>D29</td>
            <td>Programmable I/O</td>
        </tr>
        <tr>
            <td>4</td>
            <td>D19</td>
            <td>Programmable I/O</td>
            <td>18</td>
            <td>D30</td>
            <td>Programmable I/O</td>
        </tr>
        <tr>
            <td>5</td>
            <td>D20</td>
            <td>Programmable I/O</td>
            <td>19</td>
            <td>D31</td>
            <td>Programmable I/O</td>
        </tr>
        <tr>
            <td>6</td>
            <td>D21</td>
            <td>Programmable I/O</td>
            <td>20</td>
            <td>D32</td>
            <td>Programmable I/O</td>
        </tr>
        <tr>
            <td>7</td>
            <td>D22</td>
            <td>Programmable I/O</td>
            <td>21</td>
            <td>D33</td>
            <td>Programmable I/O</td>
        </tr>
        <tr>
            <td>8</td>
            <td>D23</td>
            <td>Programmable I/O</td>
            <td>22</td>
            <td>D34</td>
            <td>Programmable I/O</td>
        </tr>
        <tr>
            <td>9</td>
            <td>D24</td>
            <td>Programmable I/O</td>
            <td>23</td>
            <td>D35</td>
            <td>Programmable I/O</td>
        </tr>
        <tr>
            <td>10</td>
            <td>D25</td>
            <td>Programmable I/O</td>
            <td>24</td>
            <td>D36</td>
            <td>Programmable I/O</td>
        </tr>
        <tr>
            <td>11</td>
            <td>D26</td>
            <td>Programmable I/O</td>
            <td>25</td>
            <td>D37</td>
            <td>Programmable I/O</td>
        </tr>
        <tr>
            <td>12</td>
            <td>D27</td>
            <td>Programmable I/O</td>
            <td>26</td>
            <td>D38</td>
            <td>Programmable I/O</td>
        </tr>
        <tr>
            <td>13</td>
            <td>GND</td>
            <td>Ground</td>
            <td>27</td>
            <td>GND</td>
            <td>Ground</td>
        </tr>
        <tr>
            <td>14</td>
            <td>3V3</td>
            <td>3.3 V Power</td>
            <td>28</td>
            <td>3V3</td>
            <td>3.3 V Power</td>
        </tr>
    </tbody>
</table>


## Pin Mapping



<table>
    <colgroup>
        <col style="width: 9rem;">
        <col style="width: 9rem;">
        <col style="width: auto; min-width: 15rem;">
    </colgroup>
    <thead>
        <tr>
            <th>Pin Name</th>
            <th>Ball Number</th>
            <th>Ball Function</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>D0</td>
            <td>G1</td>
            <td>IOL_24B</td>
        </tr>
        <tr>
            <td>D1</td>
            <td>H1</td>
            <td>IOB_54</td>
        </tr>
        <tr>
            <td>D2</td>
            <td>H2</td>
            <td>IOL_26B</td>
        </tr>
        <tr>
            <td>D3</td>
            <td>J3</td>
            <td>IOB_57</td>
        </tr>
        <tr>
            <td>D4</td>
            <td>J4</td>
            <td>IOB_70</td>
        </tr>
        <tr>
            <td>D5</td>
            <td>J9</td>
            <td>IOR_110</td>
        </tr>
        <tr>
            <td>D6</td>
            <td>G9</td>
            <td>IOR_112</td>
        </tr>
        <tr>
            <td>D7</td>
            <td>D9</td>
            <td>IOR_119</td>
        </tr>
        <tr>
            <td>D8</td>
            <td>F1</td>
            <td>IOL_22A</td>
        </tr>
        <tr>
            <td>D9</td>
            <td>G4</td>
            <td>IOB_81_GBIN5</td>
        </tr>
        <tr>
            <td>D10</td>
            <td>J1</td>
            <td>IOB_55</td>
        </tr>
        <tr>
            <td>D11</td>
            <td>J2</td>
            <td>IOB_56</td>
        </tr>
        <tr>
            <td>D12</td>
            <td>H4</td>
            <td>IOB_82_GBIN4</td>
        </tr>
        <tr>
            <td>D13</td>
            <td>J8</td>
            <td>IOR_109</td>
        </tr>
        <tr>
            <td>D14</td>
            <td>H9</td>
            <td>IOR_111</td>
        </tr>
        <tr>
            <td>D15</td>
            <td>E8</td>
            <td>IOR_140_GBIN3</td>
        </tr>
        <tr>
            <td>D16</td>
            <td>E1</td>
            <td>IOL_10B</td>
        </tr>
        <tr>
            <td>D17</td>
            <td>E2</td>
            <td>IOL_13A</td>
        </tr>
        <tr>
            <td>D18</td>
            <td>D2</td>
            <td>IOL_7A</td>
        </tr>
        <tr>
            <td>D19</td>
            <td>C2</td>
            <td>IOL_2A</td>
        </tr>
        <tr>
            <td>D20</td>
            <td>A1</td>
            <td>IOT_224</td>
        </tr>
        <tr>
            <td>D21</td>
            <td>A2</td>
            <td>IOT_221</td>
        </tr>
        <tr>
            <td>D22</td>
            <td>A3</td>
            <td>IOT_217</td>
        </tr>
        <tr>
            <td>D23</td>
            <td>B5</td>
            <td>IOT_188</td> 
        </tr>
        <tr>
            <td>D24</td>
            <td>B6</td>
            <td>IOT_183</td> 
        </tr>
        <tr>
            <td>D25</td>
            <td>B7</td>
            <td>IOT_180</td> 
        </tr>
        <tr>
            <td>D26</td>
            <td>B8</td>
            <td>IOT_170</td> 
        </tr>
        <tr>
            <td>D27</td>
            <td>B9</td>
            <td>IOT_120</td> 
        </tr>
        <tr>
            <td>D28</td>
            <td>D1</td>
            <td>IOL_10A</td> 
        </tr>
        <tr>
            <td>D29</td>
            <td>C1</td>
            <td>IOL_3B</td> 
        </tr>
        <tr>
            <td>D30</td>
            <td>B1</td>
            <td>IOL_3A</td> 
        </tr>
        <tr>
            <td>D31</td>
            <td>B2</td>
            <td>IOL_2B</td> 
        </tr>
        <tr>
            <td>D32</td>
            <td>B3</td>
            <td>IOT_218</td> 
        </tr>
        <tr>
            <td>D33</td>
            <td>A4</td>
            <td>IOT_208</td> 
        </tr>
        <tr>
            <td>D34</td>
            <td>A6</td>
            <td>IOT_185</td> 
        </tr>
        <tr>
            <td>D35</td>
            <td>A7</td>
            <td>IOT_177</td> 
        </tr>
        <tr>
            <td>D36</td>
            <td>A8</td>
            <td>IOT_174</td> 
        </tr>
        <tr>
            <td>D37</td>
            <td>A9</td>
            <td>IOR_116</td> 
        </tr>
        <tr>
            <td>D38</td>
            <td>C9</td>
            <td>IOR_148</td> 
        </tr>
        <tr>
            <td>CS</td>
            <td>F7</td>
            <td>IOB_108_SS</td> 
        </tr>
        <tr>
            <td>SCK</td>
            <td>G7</td>
            <td>IOB_107_SCK</td> 
        </tr>
        <tr>
            <td>MOSI</td>
            <td>H7, G6</td>
            <td>IOB_106_SDI, IOB_105_SDO</td>
        </tr>
        <tr>
            <td>MISO</td>
            <td>G6, H7</td>
            <td>IOB_105_SDO, IOR_106_SDI</td>
        </tr>
        <tr>
            <td>CRST</td>
            <td>H6</td>
            <td>CRESET_B</td> 
        </tr>
        <tr>
            <td>CDN</td>
            <td>E6</td>
            <td>CDONE</td> 
        </tr>
    </tbody>
</table>



<!--
![Alt text](diag/jay40_pinout.svg){: }

%===============================================================
% Input/Output : Overview
%===============================================================
\subsection{Overview}
\label{sec:input/output:overview}

The Jay40 provides access to 39 of the FPGA's programmable I/O pins. These pins are exposed through the board's two 24-pin connectors and are labeled \texttt{D0} through \texttt{D38}. Each programmable I/O can be configured as an input, output, or tri-state buffer. In addition, an internal pull-up resistor can be enabled for each pin. For more detail, please refer to the "iCE40 Family Data Sheet."

The board's connectors also provide the pins required to program the FPGA and flash chip. This is done through a standard SPI interface (\texttt{CS}, \texttt{SCK}, \texttt{MOSI}, and \texttt{MISO}) and two dedicated FPGA configuration pins, \texttt{CRST} and \texttt{CDN}.

For power, the board includes several \texttt{3V3} and \texttt{GND} pins, as well as a \texttt{5V} pin. Depending on the setup, these power pins be used as either power inputs or power outputs.

%===============================================================
% Input/Output : Connector Pinout
%===============================================================
\subsection{Connector Pinout}
\label{sec:input/output:connector_pinout}

The board's pinout is shown in \autoref{fig:jay40_pinout}. Aside from the single \texttt{5V} power pin, all of the board's I/O operate at a 3.3 V logic level.

\begin{figure}[H]
    \vspace{0.6cm}
    \centering
    \includegraphics[width=12.36cm]{../../diag/export/jay40_pinout.pdf}
    \caption{Connector Pinout}
    \label{fig:jay40_pinout}
\end{figure}

{
    \vspace{0.6cm}
    \renewcommand{\arraystretch}{1.3}
    \setlength{\arrayrulewidth}{0.3mm}
    \color{tabletextcolor}
    \arrayrulecolor{tablelinecolor}
    %\begin{xltabular}{\textwidth}{|p{7mm}|p{18mm}|X!{\vrule width 0.6mm}p{7mm}|p{18mm}|X|}
    \begin{xltabular}{\textwidth}{|p{7mm}|p{18mm}|X|p{7mm}|p{18mm}|X|}
    \hline
    \rowcolor{tableheadercolor}
    \textbf{Pin} & \textbf{Pin Name} & \textbf{Description} & \textbf{Pin} & \textbf{Pin Name} & \textbf{Description} \\
    \endfirsthead
    \hline
    \rowcolor{tableheadercolor}
    \textbf{Pin} & \textbf{Pin Name} & \textbf{Description} & \textbf{Pin} & \textbf{Pin Name} & \textbf{Description} \\
    \endhead
    \hline
    1 & 3V3 & 3.3 V Power & 15 & 3V3 & 3.3 V Power \\
    \hline
    2 & GND & Ground & 16 & GND & Ground \\
    \hline
    3 & D0 & Programmable I/O & 17 & D8 & Programmable I/O \\
    \hline
    4 & D1 & Programmable I/O & 18 & D9 & Programmable I/O \\
    \hline
    5 & D2 & Programmable I/O & 19 & D10 & Programmable I/O \\
    \hline
    6 & D3 & Programmable I/O & 20 & D11 & Programmable I/O \\
    \hline
    7 & D4 & Programmable I/O & 21 & D12 & Programmable I/O \\
    \hline
    8 & D5 & Programmable I/O & 22 & D13 & Programmable I/O \\
    \hline
    9 & D6 & Programmable I/O & 23 & D14 & Programmable I/O \\
    \hline
    10 & D7 & Programmable I/O & 24 & D15 & Programmable I/O \\
    \hline
    11 & MOSI & SPI Master Out Slave In & 25 & CS & SPI Chip Select \\
    \hline
    12 & MISO & SPI Master In Slave Out & 26 & SCK & SPI Serial Clock\\
    \hline
    13 & GND & Ground & 27 & CDN & Configuration Done \\
    \hline
    14 & 3V3 & 3.3 V Power & 28 & CRST & Configuration Reset \\
    \hline
    \caption{Left Connector Pinout}
    \label{tab:left_connector_pinout}
    \end{xltabular}
}

{
    \vspace{0.6cm}
    \renewcommand{\arraystretch}{1.3}
    \setlength{\arrayrulewidth}{0.3mm}
    \color{tabletextcolor}
    \arrayrulecolor{tablelinecolor}
    \begin{xltabular}{\textwidth}{|p{7mm}|p{18mm}|X|p{7mm}|p{18mm}|X|}
    %\begin{xltabular}{\textwidth}{|p{7mm}|p{18mm}|X!{\vrule width 0.6mm}p{7mm}|p{18mm}|X|}
    \hline
    \rowcolor{tableheadercolor}
    \textbf{Pin} & \textbf{Pin Name} & \textbf{Description} & \textbf{Pin} & \textbf{Pin Name} & \textbf{Description} \\
    \endfirsthead
    \hline
    \rowcolor{tableheadercolor}
    \textbf{Pin} & \textbf{Pin Name} & \textbf{Description} & \textbf{Pin} & \textbf{Pin Name} & \textbf{Description} \\
    \endhead
    \hline
    1 & D16 & Programmable I/O & 15 & 5V & 5 V Power \\
    \hline
    2 & D17 & Programmable I/O & 16 & D28 & Programmable I/O \\
    \hline
    3 & D18 & Programmable I/O & 17 & D29 & Programmable I/O \\
    \hline
    4 & D19 & Programmable I/O & 18 & D30 & Programmable I/O \\
    \hline
    5 & D20 & Programmable I/O & 19 & D31 & Programmable I/O \\
    \hline
    6 & D21 & Programmable I/O & 20 & D32 & Programmable I/O \\
    \hline
    7 & D22 & Programmable I/O & 21 & D33 & Programmable I/O \\
    \hline
    8 & D23 & Programmable I/O & 22 & D34 & Programmable I/O \\
    \hline
    9 & D24 & Programmable I/O & 23 & D35 & Programmable I/O \\
    \hline
    10 & D25 & Programmable I/O & 24 & D36 & Programmable I/O \\
    \hline
    11 & D26 & Programmable I/O & 25 & D37 & Programmable I/O \\
    \hline
    12 & D27 & Programmable I/O & 26 & D38 & Programmable I/O \\
    \hline
    13 & GND & Ground & 27 & GND & Ground \\
    \hline
    14 & 3V3 & 3.3 V Power & 28 & 3V3 & 3.3 V Power \\
    \hline
    \caption{Right Connector Pinout}
    \label{tab:right_connector_pinout}
    \end{xltabular}
}

%===============================================================
% Input/Output : Pin Mapping 
%===============================================================
\subsection{Pin Mapping}
\label{sec:input/output:pin_mapping}

The Jay40 breaks out 39 of the FPGA's programmable I/O pins, which are connected to the header pins \texttt{D0} through \texttt{D38}. When programming the FPGA, the inputs and outputs of the RTL design must be mapped to physical pins on the FPGA. This information must be specified in a pin constraints file (\texttt{.pcf}) which is fed into the place-and-route tool as part of the bitstream generation flow. The FPGA pins should be choose such that they map to the desired header pins on the Jay40. 

\autoref{tab:pin_mapping} provides a mapping between the board's header pins and the pins of the FPGA. For reference, the Jay40 uses the iCE40LP8K-CM81 FPGA, which comes in 81-ball ucBGA package. The balls are laid out in a 9x9 grid array, with each ball designated by a row letter, "A" through "J" (the letter "I" is skipped), and a column number. 

{
    \vspace{0.6cm}
    \renewcommand{\arraystretch}{1.5}
    \setlength{\arrayrulewidth}{0.3mm}
    \color{tabletextcolor}
    \arrayrulecolor{tablelinecolor}
    \begin{xltabular}{\textwidth}{|p{9mm}|p{14mm}|X|p{9mm}|p{14mm}|X|}
    %\begin{xltabular}{\textwidth}{|p{9mm}|p{10mm}|X!{\vrule width 0.6mm}p{9mm}|p{10mm}|X|}
    \hline
    \rowcolor{tableheadercolor}
    \textbf{Pin Name} & \textbf{Ball Number} & \textbf{Ball Function} & \textbf{Pin Name} & \textbf{Ball Number} & \textbf{Ball Function} \\
    \endfirsthead
    \hline
    \rowcolor{tableheadercolor}
    \textbf{Pin Name} & \textbf{Ball Number} & \textbf{Ball Function} & \textbf{Pin Name} & \textbf{Ball Number} & \textbf{Ball Function} \\
    \endhead
    \hline
    D0 & G1 & IOL\_24B & D23 & B5 & IOT\_188 \\ 
    \hline
    D1 & H1 & IOB\_54 & D24 & B6 & IOT\_183 \\ 
    \hline
    D2 & H2 & IOL\_26B & D25 & B7 & IOT\_180 \\ 
    \hline
    D3 & J3 & IOB\_57 & D26 & B8 & IOT\_170 \\ 
    \hline
    D4 & J4 & IOB\_70 & D27 & B9 & IOT\_120 \\ 
    \hline
    D5 & J9 & IOR\_110 & D28 & D1 & IOL\_10A \\ 
    \hline
    D6 & G9 & IOR\_112 & D29 & C1 & IOL\_3B \\ 
    \hline
    D7 & D9 & IOR\_119 & D30 & B1 & IOL\_3A \\ 
    \hline
    D8 & F1 & IOL\_22A & D31 & B2 & IOL\_2B \\ 
    \hline
    D9 & G4 & IOB\_81\_GBIN5 & D32 & B3 & IOT\_218 \\ 
    \hline
    D10 & J1 & IOB\_55 & D33 & A4 & IOT\_208 \\ 
    \hline
    D11 & J2 & IOB\_56 & D34 & A6 & IOT\_185 \\ 
    \hline
    D12 & H4 & IOB\_82\_GBIN4 & D35 & A7 & IOT\_177 \\ 
    \hline
    D13 & J8 & IOR\_109 & D36 & A8 & IOT\_174 \\ 
    \hline
    D14 & H9 & IOR\_111 & D37 & A9 & IOR\_116 \\ 
    \hline
    D15 & E8 & IOR\_140\_GBIN3 & D38 & C9 & IOR\_148 \\ 
    \hline
    D16 & E1 & IOL\_10B & CS & F7 & IOB\_108\_SS \\ 
    \hline
    D17 & E2 & IOL\_13A & SCK & G7 & IOB\_107\_SCK \\ 
    \hline
    D18 & D2 & IOL\_7A & MOSI & H7, G6 & IOB\_106\_SDI, IOB\_105\_SDO \\ 
    \hline
    D19 & C2 & IOL\_2A & MISO & G6, H7 & IOR\_105\_SDO, IOR\_106\_SDI \\ 
    \hline
    D20 & A1 & IOT\_224 & CRST & H6 & CRESET\_B \\ 
    \hline
    D21 & A2 & IOT\_221 & CDN & E6 & CDONE \\ 
    \hline
    D22 & A3 & IOT\_217 & & & \\ 
    \hline
    \caption{Header Pin to FPGA Pin Mapping}
    \label{tab:pin_mapping}
    \end{xltabular}
}

Note, for the MOSI and MISO header pins, their connections to the FPGA's pins depend on the configuration mode. 

In addition to the header pins listed in Table \autoref{tab:pin_mapping}, another important connection to know is that between the FPGA and the board's oscillator. The Jay40 includes a 12 MHz MEMS oscillator which can provide a clock signal for the FPGA. The 12 MHz output of the oscillator is connected to ball \texttt{C4} (\texttt{IOT\_198\_GBIN0}) of the FPGA. This information will be required to specify the clock input in a pin constraints file.

%MEMS oscilator which produces a 12 MHz square wave which can be used as a clock signal for the FPGA. This 12 MHz clock signal is connected to pin C4 (IOT\_198\_GBIN0) of the FPGA. This information is needed when specifing the clock input in the .pcf file.

<table>
  <colgroup>
    <col style="width: 4rem;">
    <col style="width: 7rem;">
    <col style="width: auto; min-width: 10rem;">
    <col style="width: 4rem;">
    <col style="width: 7rem;">
    <col style="width: auto; min-width: 10rem;">
  </colgroup>
  <thead>
    <tr>
      <th>Pin</th>
      <th>Pin Name</th>
      <th>Description</th>
      <th>Pin</th>
      <th>Pin Name</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>3V3</td>
      <td>3.3 V Power</td>
      <td>1</td>
      <td>3V3</td>
      <td>3.3 V Power</td>
    </tr>
    <tr>
      <td>2</td>
      <td>GND</td>
      <td>Ground</td>
      <td>2</td>
      <td>GND</td>
      <td>Ground</td>
    </tr>
    <tr>
      <td>3</td>
      <td>D0</td>
      <td>Programmable I/O</td>
      <td>3</td>
      <td>D0</td>
      <td>Programmable I/O</td>
    </tr>
    <tr>
      <td>4</td>
      <td>D1</td>
      <td>Programmable I/O</td>
      <td>3</td>
      <td>D0</td>
      <td>Programmable I/O</td>
    </tr>
    <tr>
      <td>5</td>
      <td>D2</td>
      <td>Programmable I/O</td>
      <td>3</td>
      <td>D0</td>
      <td>Programmable I/O</td>
    </tr>
  </tbody>
</table>

| Pin | Pin Name | Description |
|----------|----------|----------|
| 1    | 3V3 | 3.3 V Power |
| 2    | GND | Ground |
| 3    | D0 | Programmable I/O |

<table>
  <colgroup>
    <col style="width: 10rem;">
    <col style="width: 10rem;">
    <col style="width: auto; min-width: 10rem;">
  </colgroup>
  <thead>
    <tr>
      <th>Pin</th>
      <th>Pin Name</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>3V3</td>
      <td>3.3 V Power</td>
    </tr>
    <tr>
      <td>2</td>
      <td>GND</td>
      <td>Ground</td>
    </tr>
    <tr>
      <td>3</td>
      <td>D0</td>
      <td>Programmable I/O</td>
    </tr>
    <tr>
      <td>4</td>
      <td>D1</td>
      <td>Programmable I/O</td>
    </tr>
    <tr>
      <td>5</td>
      <td>D2</td>
      <td>Programmable I/O</td>
    </tr>
    <tr>
      <td>6</td>
      <td>D3</td>
      <td>Programmable I/O</td>
    </tr>
    <tr>
      <td>7</td>
      <td>D4</td>
      <td>Programmable I/O</td>
    </tr>
    <tr>
      <td>8</td>
      <td>D5</td>
      <td>Programmable I/O</td>
    </tr>
    <tr>
      <td>9</td>
      <td>D6</td>
      <td>Programmable I/O</td>
    </tr>
    <tr>
      <td>10</td>
      <td>D7</td>
      <td>Programmable I/O</td>
    </tr>
    <tr>
      <td>11</td>
      <td>MOSI</td>
      <td>SPI Master Out Slave In</td>
    </tr>
    <tr>
      <td>12</td>
      <td>MISO</td>
      <td>SPI Master In Slave Out</td>
    </tr>
    <tr>
      <td>13</td>
      <td>GND</td>
      <td>Ground</td>
    </tr>
    <tr>
      <td>14</td>
      <td>3V3</td>
      <td>3.3 V Power</td>
    </tr>
    <tr>
      <td>15</td>
      <td>3V3</td>
      <td>3.3 V Power</td>
    </tr>
    <tr>
      <td>16</td>
      <td>GND</td>
      <td>Ground</td>
    </tr>
    <tr>
      <td>17</td>
      <td>D8</td>
      <td>Programmable I/O</td>
    </tr>
    <tr>
      <td>17</td>
      <td>D8</td>
      <td>Programmable I/O</td>
    </tr>
    <tr>
      <td>17</td>
      <td>D8</td>
      <td>Programmable I/O</td>
    </tr>
    <tr>
      <td>18</td>
      <td>D9</td>
      <td>Programmable I/O</td>
    </tr>
    <tr>
      <td>19</td>
      <td>D10</td>
      <td>Programmable I/O</td>
    </tr>
    <tr>
      <td>20</td>
      <td>D11</td>
      <td>Programmable I/O</td>
    </tr>
    <tr>
      <td>21</td>
      <td>D12</td>
      <td>Programmable I/O</td>
    </tr>
    <tr>
      <td>22</td>
      <td>D13</td>
      <td>Programmable I/O</td>
    </tr>
    <tr>
      <td>23</td>
      <td>D14</td>
      <td>Programmable I/O</td>
    </tr>
    <tr>
      <td>17</td>
      <td>D8</td>
      <td>Programmable I/O</td>
    </tr>
    <tr>
      <td>17</td>
      <td>D8</td>
      <td>Programmable I/O</td>
    </tr>
  </tbody>
</table>

<table>
    <colgroup>
        <col style="width: 7rem;">
        <col style="width: 8rem;">
        <col style="width: auto; min-width: 9rem;">
        <col style="width: 7rem;">
        <col style="width: 8rem;">
        <col style="width: auto; min-width: 9rem;">
    </colgroup>
    <thead>
        <tr>
            <th>Pin Name</th>
            <th>Ball Number</th>
            <th>Ball Function</th>
            <th>Pin Name</th>
            <th>Ball Number</th>
            <th>Ball Function</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>D0</td>
            <td>G1</td>
            <td>IOL_24B</td>
            <td>D23</td>
            <td>B5</td>
            <td>IOT_188</td> 
        </tr>
        <tr>
            <td>D1</td>
            <td>H1</td>
            <td>IOB_54</td>
            <td>D24</td>
            <td>B6</td>
            <td>IOT_183</td> 
        </tr>
        <tr>
            <td>D2</td>
            <td>H2</td>
            <td>IOL_26B</td>
            <td>D25</td>
            <td>B7</td>
            <td>IOT_180</td> 
        </tr>
        <tr>
            <td>D3</td>
            <td>J3</td>
            <td>IOB_57</td>
            <td>D26</td>
            <td>B8</td>
            <td>IOT_170</td> 
        </tr>
        <tr>
            <td>D4</td>
            <td>J4</td>
            <td>IOB_70</td>
            <td>D27</td>
            <td>B9</td>
            <td>IOT_120</td> 
        </tr>
        <tr>
            <td>D5</td>
            <td>J9</td>
            <td>IOR_110</td>
            <td>D28</td>
            <td>D1</td>
            <td>IOL_10A</td> 
        </tr>
        <tr>
            <td>D6</td>
            <td>G9</td>
            <td>IOR_112</td>
            <td>D29</td>
            <td>C1</td>
            <td>IOL_3B</td> 
        </tr>
        <tr>
            <td>D7</td>
            <td>D9</td>
            <td>IOR_119</td>
            <td>D30</td>
            <td>B1</td>
            <td>IOL_3A</td> 
        </tr>
        <tr>
            <td>D8</td>
            <td>F1</td>
            <td>IOL_22A</td>
            <td>D31</td>
            <td>B2</td>
            <td>IOL_2B</td> 
        </tr>
        <tr>
            <td>D9</td>
            <td>G4</td>
            <td>IOB_81_GBIN5</td>
            <td>D32</td>
            <td>B3</td>
            <td>IOT_218</td> 
        </tr>
        <tr>
            <td>D10</td>
            <td>J1</td>
            <td>IOB_55</td>
            <td>D33</td>
            <td>A4</td>
            <td>IOT_208</td> 
        </tr>
        <tr>
            <td>D11</td>
            <td>J2</td>
            <td>IOB_56</td>
            <td>D34</td>
            <td>A6</td>
            <td>IOT_185</td> 
        </tr>
        <tr>
            <td>D12</td>
            <td>H4</td>
            <td>IOB_82_GBIN4</td>
            <td>D35</td>
            <td>A7</td>
            <td>IOT_177</td> 
        </tr>
        <tr>
            <td>D13</td>
            <td>J8</td>
            <td>IOR_109</td>
            <td>D36</td>
            <td>A8</td>
            <td>IOT_174</td> 
        </tr>
        <tr>
            <td>D14</td>
            <td>H9</td>
            <td>IOR_111</td>
            <td>D37</td>
            <td>A9</td>
            <td>IOR_116</td> 
        </tr>
        <tr>
            <td>D15</td>
            <td>E8</td>
            <td>IOR_140_GBIN3</td>
            <td>D38</td>
            <td>C9</td>
            <td>IOR_148</td> 
        </tr>
        <tr>
            <td>D16</td>
            <td>E1</td>
            <td>IOL_10B</td>
            <td>CS</td>
            <td>F7</td>
            <td>IOB_108_SS</td> 
        </tr>
        <tr>
            <td>D17</td>
            <td>E2</td>
            <td>IOL_13A</td>
            <td>SCK</td>
            <td>G7</td>
            <td>IOB_107_SCK</td> 
        </tr>
        <tr>
            <td>D18</td>
            <td>D2</td>
            <td>IOL_7A</td>
            <td>MOSI</td>
            <td>H7,</td>
            <td>IOB_105_SDO</td>
        </tr>
        <tr>
            <td>D19</td>
            <td>C2</td>
            <td>IOL_2A</td>
            <td>MISO</td>
            <td>G6,</td>
            <td>IOR_106_SDI</td>
        </tr>
        <tr>
            <td>D20</td>
            <td>A1</td>
            <td>IOT_224</td>
            <td>CRST</td>
            <td>H6</td>
            <td>CRESET_B</td> 
        </tr>
        <tr>
            <td>D21</td>
            <td>A2</td>
            <td>IOT_221</td>
            <td>CDN</td>
            <td>E6</td>
            <td>CDONE</td> 
        </tr>
        <tr>
            <td>D22</td>
            <td>A3</td>
            <td>IOT_217</td>
            <td></td>
            <td></td>
            <td></td> 
        </tr>
    </tbody>
</table>

-->
