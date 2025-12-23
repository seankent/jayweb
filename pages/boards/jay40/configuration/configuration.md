# Configuration 

## Overview


![Alt text](diag/jay40_cfg_if_highlight.svg){: style="width: 30rem;"}

![Alt text](diag/jay40_cfg_sel_highlight.svg){: style="width: 30rem;"}

![Alt text](diag/jay40_cfg_sel_cutout_flash.svg){: style="width: 13rem;"}

![Alt text](diag/jay40_cfg_sel_cutout_fpga.svg){: style="width: 13rem;"}

![Alt text](diag/jay40_cfg_sel_circuit_flash.svg){: style="width: 40rem;"}

![Alt text](diag/jay40_cfg_sel_circuit_fpga.svg){: style="width: 40rem;"}

<!--
![Alt text](diag/jay40_cfg_if_highlight.pdf){: style="width: 30rem;"}

%===============================================================
% Configuration 
%===============================================================
\newpage
\section{Configuration}
\label{sec:configuration}

%===============================================================
% Configuration : Overview
%===============================================================
\subsection{Overview}
\label{sec:configuration:overview}

The iCE40LP8K is an SRAM-based FPGA, which means its configuration is stored in SRAM memory cells distributed throughout the chip. These cells are volatile and thus lose their contents when power is removed. While the use of SRAM cells allows the FPGA to be easily programmed, it also means the configuration must be reloaded each time the device is powered on.

The FPGA supports two primary configuration modes: Master Configuration Mode and Slave Configuration Mode. In Master Configuration Mode, the FPGA automatically loads its configuration from the onboard SPI flash chip when power is applied. In Slave Configuration Mode, an external programmer directly loads the configuration into the FPGA. 

The following subsections explain how to set up and use both configuration modes. They also discuss how to program the flash chip, which allows the bitstream to be stored permanently on the board. 

%===============================================================
% Configuration : Configuration Interface 
%===============================================================
\subsection{Configuration Interface}
\label{sec:configuration:configuration_interface}

The FPGA's bitstream is loaded through a standard SPI interface. In addition, the FPGA has two dedicated configuration pins, \texttt{CRESET\_B} and \texttt{CDONE}, which assist in the configuration process. \texttt{CRESET\_B} is an active-low input that resets the FPGA's configuration. \texttt{CDONE} is an output of the FPGA and is asserted when the configuration has been successfully loaded. 

The Jay40's configuration interface is located at the bottom of the left 24-pin connector as shown in \autoref{fig:jay40_cfg_if_highlight}. This interface includes the four SPI signals, as well as the two FPGA-specific configuration pins, \texttt{CRESET\_B} and \texttt{CDONE}. These are abbreviated \texttt{CRST} and \texttt{CDN} on the board. The configuration interface can be used to program both the FPGA and the flash chip.

When connecting an external programmer to the board, it is expected that both devices operate off of the same 3.3 V supply. This can be achieved by powering the Jay40 from the external programmer's power supply through the \texttt{3V3} and \texttt{GND} pins. Note, the \texttt{PWR SEL} jumper should always be disconnected when powering the Jay40 from an external 3.3 V source. See \autoref{sec:power} for more details on supplying power to the board.


%\begin{figure}[H]
%    \vspace{0.6cm}
%    \centering
%%%skent%%    \includegraphics[width=12.36cm]{configuration_ice40lp8k_development_board.pdf}
%    \caption{Configuration Interface}
%    \label{fig:configuration_interface}
%\end{figure}

\begin{figure}[H]
    \centering
    %\includegraphics[width=\textwidth]{../../diag/export/jay40_led_highlight.pdf}
    \vspace{0.6cm}
    \includegraphics[width=12cm]{../../diag/export/jay40_cfg_if_highlight.pdf}
    \vspace{0.6cm}
    \caption{Configuration Interface}
    \label{fig:jay40_cfg_if_highlight}
\end{figure}



%The board's configuration interface can also be used to program the SPI flash chip. This allows a bitstream image to be written into the flash's memory. 

%===============================================================
% Configuration : Configuration Jumpers
%===============================================================
\subsection{Configuration Jumpers}
\label{sec:configuration:configuration_jumpers}

The SPI connections required on the board are different depending on what operation is being performed. In Master Configuration Mode, the FPGA is the SPI master the flash chip is the SPI slave. In Slave Configuration Mode, the external programmer is the SPI master and the FPGA is the SPI slave. When programming the flash, the external programmer is the SPI master and the flash chip is the SPI slave.

To support all these modes, the Jay40 has a set of configuration jumpers which modify the SPI connections as needed. These jumpers are labeled \texttt{CFG SEL} in \autoref{fig:jay40_cfg_sel_highlight}.

The Jay40's configuration jumpers have two valid settings: FLASH and FPGA. These two settings are sufficient for supporting the three operations mentioned above (Master Configuration Mode, Slave Configuration Mode, and flash programming). The jumper positions for the two settings are shown in \autoref{fig:jay40_cfg_sel_cutout_flash} and \autoref{fig:jay40_cfg_sel_cutout_fpga}.

\begin{figure}[H]
    \centering
    \begin{minipage}{0.68\textwidth}
        \centering
        \includegraphics[width=10cm]{../../diag/export/jay40_cfg_sel_highlight.pdf}
        \caption{\texttt{CFG SEL} Location}
        \label{fig:jay40_cfg_sel_highlight}
    \end{minipage}
    \hfill
    \begin{minipage}{0.3\textwidth}
        \centering
        \includegraphics[width=4cm]{../../diag/export/jay40_cfg_sel_cutout_flash.pdf}
        \caption{FLASH Setting}
        \label{fig:jay40_cfg_sel_cutout_flash}
        \vspace{0.5cm}
        \includegraphics[width=4cm]{../../diag/export/jay40_cfg_sel_cutout_fpga.pdf}
        \caption{FPGA Setting}
        \label{fig:jay40_cfg_sel_cutout_fpga}
    \end{minipage}
\end{figure}



%===============================================================
% Configuration : FLASH Jumper Setting 
%===============================================================
\subsection{FLASH Jumper Setting}
\label{sec:configuration:flash_setting}

The FLASH jumper setting is used for operating the FPGA in Master Configuration Mode and for programming the flash chip. \autoref{fig:jay40_cfg_sel_circuit_flash} shows the SPI connections when the jumpers are in the FLASH position. 

In this configuration, the \texttt{SPI\_SS}, \texttt{SPI\_SCK}, \texttt{SPI\_SO}, and \texttt{SPI\_SI} pins of the FPGA are connected to the \texttt{CS}, \texttt{SCK}, \texttt{SI}, and \texttt{SO} pins of the flash. This establishes the SPI connections to allow the FPGA to send commands and read data from the flash.

The SPI pins of the Jay40 also connect to the \texttt{CS}, \texttt{SCK}, \texttt{SI}, and \texttt{SO} pins of the flash chip. This enables an external programmer to access and program the flash.

When programming the flash chip, the \texttt{CRESET\_B} pin of the FPGA must be held low. This puts the FPGA into reset and prevents it from interfering with flash programming sequence. It also puts the FPGA's SPI pins in a high-impedance state.

\begin{figure}[H]
    \centering
    \vspace{0.6cm}
    \includegraphics[width=13cm]{../../diag/export/jay40_cfg_sel_circuit_flash.pdf}
    \vspace{0.6cm}
    \caption{Flash Setting Circuit Diagram}
    \label{fig:jay40_cfg_sel_circuit_flash}
\end{figure}

%===============================================================
% Configuration : FPGA Jumper Setting 
%===============================================================
\subsection{FPGA Jumper Setting}
\label{sec:configuration:fpga_setting}

The FPGA jumper setting is use for operating the FPGA in Slave Configuration Mode. \autoref{fig:jay40_cfg_sel_circuit_fpga} shows the SPI connections when the jumpers are in the FPGA position.

In this configuration, the board's MOSI and MISO pins are connected to the FPGA's \texttt{SPI\_SI} and \texttt{SPI\_SO} pins. This allows an external programmer to write data into the FPGA. In addition, the \texttt{CS} pin of the flash chip is disconnected from the board's \texttt{CS} pin and pulled high by a 10 k\textOmega\ pull-up resistor. This keeps the flash in a de-selected state and prevents the signaling between the external programmer and the FPGA from accidentally modifying its contents.

\begin{figure}[H]
    \centering
    \vspace{0.6cm}
    \includegraphics[width=13cm]{../../diag/export/jay40_cfg_sel_circuit_fpga.pdf}
    \vspace{0.6cm}
    \caption{FPGA Setting Circuit Diagram}
    \label{fig:jay40_cfg_sel_circuit_fpga}
\end{figure}

%===============================================================
% Configuration : Master Configuration Mode 
%===============================================================
\subsection{Master Configuration Mode}
\label{sec:configuration:master_configuration_mode}

In Master Configuration Mode, the FPGA automatically configures itself from the flash chip when power is applied or \texttt{CRESET\_B} is de-asserted. In this mode, the FPGA acts as a SPI master and reads the configuration from the flash chip. By storing the FPGA's configuration in an onboard, non-volatile memory the FPGA is able to configure itself and operate without having to be connected to an external programmer.

When operating the FPGA in Master Configuration Mode, the three configuration jumpers should be placed in the "FLASH" position as shown in \autoref{fig:jay40_cfg_sel_cutout_flash}. 

When power is applied to the board, the \texttt{CRESET\_B} pin of the FPGA will be pulled high by a 10 k\textOmega\ pull-up resistors. This brings the FPGA out of reset. The FPGA will then sample the value of its \texttt{SPI\_SS} pin. With no external programmer connected, the \texttt{SPI\_SS} pin will also be pulled high by a 10 k\textOmega\ pull-up resistor. The FPGA will therefore read a logic high and enter Master Configuration Mode. The FPGA then begins the auto-configuration sequence. It starts by sending a wakeup command to the flash, then begins reading the bitstream starting at address 0x0. Once all the configuration has been loaded, the FPGA will send a "deep power-down" command to the flash to put it into a low power state. Finally, FPGA will drive its \texttt{CDONE} pin high to indicate a successful configuration.

For more details on the Master Configuration Mode, please refer to the "iCE40 Programming and Configuration" manual.

%===============================================================
% Configuration : Slave Configuration Mode 
%===============================================================
\subsection{Slave Configuration Mode}
\label{sec:configuration:slave_configuration_mode}

In Slave Configuration Mode, an external programmer loads the configuration onto the FPGA. This mode allows the FPGA to be quickly programmed and reprogrammed, which can be useful when prototyping and debugging. Slave Configuration Mode can also be useful when the device is integrated into a larger system where an application processor can store and load the configuration.

To program the FPGA in Slave Configuration Mode, the three configuration jumpers should be placed in the "FPGA" position as shown in \autoref{fig:jay40_cfg_sel_cutout_fpga}.

To put the FPGA into Slave Configuration Mode, the external programmer will first reset the FPGA by driving the \texttt{CRESET\_B} pin low. It will also drive the \texttt{SPI\_SS} pin low. The external programmer will then release \texttt{CRESET\_B} while keeping \texttt{SPI\_SS} held low. When the FPGA comes out of reset, it will sample the \texttt{SPI\_SS} pin. Upon reading a logic low, the FPGA enters Slave Configuration Mode. The external programmer can then load the bitstream onto the device. Once the configuration has been loaded, the FPGA will drive its \texttt{CDONE} pin high to indicate the process has completed. 

For more details on the Slave Configuration Mode, please refer to the "iCE40 Programming and Configuration" manual.

%===============================================================
% Configuration : SPI Flash Programming 
%===============================================================
\subsection{SPI Flash Programming}
\label{sec:configuration:spi_flash_programming}

Before the FPGA can operate in Master Configuration Mode, a bitstream image must be written into the flash's memory. This can be done using an external programmer attached to the Jay40's configuration interface.

The Jay40 includes a 2 Mbit flash chip, the AT25DF021, for storing the bitstream image. The size of the bitstream image for the iCE40LP8K is 1,081,464 bits.

To program the flash chip, the three configuration jumpers should be placed in the "FLASH" position as shown in \autoref{fig:jay40_cfg_sel_cutout_flash}. Note, this is the same setting used when operating the FPGA in Master Configuration Mode. However, in this case, an external programmer will need to be connected to the board. 

To program the flash, the external programmer must first put the FPGA into reset by asserting \texttt{CRESET\_B}. It can then erase, program, and verify the flash's contents using standard SPI flash commands. When the flash programming is complete, the external programmer can release \texttt{CRESET\_B}. However, it is important that any SPI outputs of the external programmer are first put into a high-impedance state or disconnected from the board. In general, this is true whenever an external programmer is attached to the board and \texttt{CRESET\_B} is de-asserted.

Once \texttt{CRESET\_B} is de-asserted, the FPGA will enter Master Configuration Mode and read in the new bitstream from the flash.

For more details on programming the flash chip, please refer to the AT25DF021 datasheet.

%===============================================================
% Configuration : Summary
%===============================================================
\subsection{Summary}
\label{sec:configuration:summary}

A summary of the configuration and programming operations is provided in \autoref{tab:configuration_and_programming_summary}.

{
\vspace{0.6cm}
\renewcommand{\arraystretch}{1.3}
\setlength{\arrayrulewidth}{0.3mm}
\color{tabletextcolor}
\arrayrulecolor{tablelinecolor}
%\begin{xltabular}{\textwidth}{|X|X|X|}
\begin{xltabular}{\textwidth}{|p{22mm}|p{50mm}|X|}
%\begin{xltabular}{\textwidth}{|p{25mm}|X|X|}
%\begin{xltabular}{\textwidth}{|X|X|p{20mm}|{}|X|}
\hline
\rowcolor{tableheadercolor}
%\textbf{Operation} & \textbf{Description} & \textbf{CONFIG SEL Setting} & \textbf{PWR SEL Setting} & \textbf{Additional Requirements} \\
\textbf{Operation} & \textbf{Description} & \textbf{Requirements} \\
\endfirsthead
\hline
\rowcolor{tableheadercolor}
\textbf{Operation} & \textbf{Description} & \textbf{Requirements} \\
\endhead
\hline
%Master\newline Configuration\newline Mode & FPGA loads configuration from flash & \\ 
%Master Configuration Mode & The FPGA loads its configuration from the flash. & \textbullet The configuration jumpers are in the "FLASH" position. \\ 
%Master Configuration Mode & The FPGA loads its configuration from the flash. & {\large\textbullet~}The configuration jumpers are in the "FLASH" position.\newline \\ 
Master\newline Configuration\newline Mode & The FPGA loads its configuration from the flash. & \vspace{-0.5em}{\begin{itemize}[parsep=2pt, leftmargin=1em] \item[$\bullet$] The configuration jumpers are in the "FLASH" position. \end{itemize}}\vspace{0.3em} \\
\hline
%Slave Configuration Mode & An external programmer configures the FPGA. & {\large\textbullet~}The configuration jumpers are in the "FPGA" position.\newline\newline {\large\textbullet~}The board is powered by the external programmer. \newline\newline {\large\textbullet~}The PWR SEL jumper is disconnected.\newline \\ 
Slave\newline Configuration\newline Mode & An external programmer configures the FPGA. & \vspace{-0.5em}{\begin{itemize}[parsep=2pt, leftmargin=1em] \item[$\bullet$] The configuration jumpers are in the "FPGA" position. \item[$\bullet$] The board is powered by the external programmer. \item[$\bullet$] The PWR SEL jumper is disconnected. \end{itemize}}\vspace{0.3em} \\ 
\hline
SPI Flash\newline Programming & An external programmer programs the flash. & \vspace{-0.5em}{\begin{itemize}[parsep=2pt, leftmargin=1em] \item[$\bullet$] The configuration jumpers are in the "FLASH" position. \item[$\bullet$] The board is powered by the external programmer. \item[$\bullet$] The PWR SEL jumper is disconnected. \item[$\bullet$] The CRESET\_B pin is held low during the programming sequence. \end{itemize}}\vspace{0.3em} \\ 
\hline
\caption{Configuration and Programming Summary}
\label{tab:configuration_and_programming_summary}
\end{xltabular}
}


-->
