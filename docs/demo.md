# Demo


# macOS Software Installation 

To install IceStorm, run the commands in... 

```bash
$ git clone https://github.com/YosysHQ/icestorm.git icestorm
$ cd icestorm
$ make -j$(nproc)
$ sudo make install
```


To install NextPNR, run the commands in...

```
$ git clone --recursive https://github.com/YosysHQ/nextpnr nextpnr
$ cd nextpnr
$ cmake . -B build -DARCH=ice40
$ cmake --build build 
$ sudo cmake --install build
```

To install Yosys, run the commands in 

```
$ git clone https://github.com/YosysHQ/yosys.git yosys
$ cd yosys
$ make -j$(nproc)
$ sudo make install
```

Note, the cloned repositories can be deleted after the tools have been installed. 

![Alt text](../docs/diag/jay40.svg){: style="width: 300px;"}

![Alt text](../docs/diag/jay40.svg)
-->

<!--
%===============================================================
% Software : Overview
%===============================================================
\subsection{Overview}
\label{sec:software:overview}

Bitstreams for the iCE40 FPGAs can be generated using a suite of free and open-source tools from Yosys and Project IceStorm. The bitstream generation flow consists of three main components: Yosys for logic synthesis, NextPNR for place-and-route, and IceStorm's IcePack for generating the final bitstream. Together, these tools combine to form a complete RTL-to-bitstream toolchain.

Project IceStorm also provides a number of other useful tools for working with iCE40 bitstreams. One such tool is IceProg, which can be used with an FTDI-based programmer to load bitstreams into iCE40 FPGAs or flash chips.

For more details on each of these tools, please refer to their respective documentation which can be found online. \autoref{sec:getting_started_demo} contains a step-by-step walkthrough of the bitstream generation flow. It also includes instructions on how to load a bitstream onto the FPGA.

%===============================================================
% Software : Linux Installation (Ubuntu) 
%===============================================================
\subsection{Linux (Ubuntu 22.04) Installation}
\label{sec:software:linux_installation}

The following commands can be used to install Yosys, NextPNR, and IceStorm on Ubuntu.

{
\vspace{0.6cm}
\begin{lstlisting}[language=bash, caption=Linux Installation Commands, label=lst:linux_installation_commands]
$ sudo apt install yosys
$ sudo apt install nextpnr-ice40 
$ sudo apt install fpga-icestorm
\end{lstlisting}
}

These commands are verified for Ubuntu 22.04. If you are running an older version of Ubuntu, the installation instructions may be different. In these cases, please refer to each tool's documentation for installation instructions. %Pointer can be found in Section TODO.

%%If you are running a different version of Ubuntu, particularly an older version, the installation commands may be different. Please refer to each tool's documentation for installation instructions.


%===============================================================
% Software : macOS Installation 
%===============================================================
\subsection{macOS Installation}
\label{sec:software:macos_installation}

%WARNING: This section is not complete. The macOS install does not work yet.
%
%For macOS, we recommend using Homebrew to install Yosys, NextPNR, and IceStorm. This can be done with the following commands.
%
%% [LISTING] Pin Constraint File Example
%{
%\vspace{0.6cm}
%\begin{lstlisting}[language=bash, caption=Pin Constraint File Example, label=lst:pin_constraint_file_example]
%$ brew install icestorm
%$ brew install nextpnr
%$ brew install yosys 
%\end{lstlisting}
%}
%
%It appears that nextpnr cannot be installed with Homebrew. The following commands may be a work-around in the future, but they don't work yet.  
%
%{
%\vspace{0.6cm}
%\begin{lstlisting}[language=bash, caption=Pin Constraint File Example, label=lst:pin_constraint_file_example]
%$ brew tap ktemkin/oss-fpga
%$ brew install --HEAD icestorm yosys nextpnr-ice40
%\end{lstlisting}
%}

For macOS, we recommend building the tools from source.

To start, please install the required dependencies using Homebrew. This can be done with the following command.

{
\vspace{0.6cm}
\begin{lstlisting}[language=bash, caption=Dependencies Installation (macOS), label=lst:dependencies_installation_macos]
$ brew install cmake python boost eigen bison flex gawk libffi pkg-config readline tcl-tk libftdi
\end{lstlisting}
}

To install IceStorm, run the commands in \autoref{lst:icestorm_installation_macos}.

{
\vspace{0.6cm}
\begin{lstlisting}[language=bash, caption=IceStorm Installation (macOS), label=lst:icestorm_installation_macos]
$ git clone https://github.com/YosysHQ/icestorm.git icestorm
$ cd icestorm
$ make -j$(nproc)
$ sudo make install
\end{lstlisting}
}

%To install NextPNR, run the commands in \autoref{lst:nextpnr_installation_macos}.

{
\vspace{0.6cm}
\begin{lstlisting}[language=bash, caption=NextPNR Installation (macOS), label=lst:nextpnr_installation_macos]
$ git clone --recursive https://github.com/YosysHQ/nextpnr nextpnr
$ cd nextpnr
$ cmake . -B build -DARCH=ice40
$ cmake --build build 
$ sudo cmake --install build
\end{lstlisting}
}

To install Yosys, run the commands in \autoref{lst:yosys_installation_macos} 

{
\vspace{0.6cm}
\begin{lstlisting}[language=bash, caption=Yosys Installation (macOS), label=lst:yosys_installation_macos]
$ git clone https://github.com/YosysHQ/yosys.git yosys
$ cd yosys
$ make -j$(nproc)
$ sudo make install
\end{lstlisting}
}

Note, the cloned repositories can be deleted after the tools have been installed. 


%===============================================================
% Software : Windows Installation 
%===============================================================
\subsection{Windows Installation}
\label{sec:software:windows_installation}

Unfortunately, not all of the tools required to generate iCE40 bitstreams run natively on Windows. For users running Windows, we recommend using Windows Subsystem for Linux (WSL). WSL lets users install a Linux distribution (such as Ubuntu) and use Linux applications, utilities, and command-line tools directly on Windows. Instruction on how to install and use WSL can be found on Microsoft's website (\href{https://learn.microsoft.com/en-us/windows/wsl/install}{https://learn.microsoft.com/en-us/windows/wsl/install}). We recommend installing Ubuntu 22.04 or later. In addition, make sure to use WSL 2 for the install. 

% Once you have WSL up and running, run the follow the commands in the WSL shell \autoref{sec:software:windows_installation_commands} to install the necessary tools.

Once you have WSL set up, run the following the commands in the WSL shell to install the bitstream tools.

% Windows Installation Commands
{
\vspace{0.6cm}
\begin{lstlisting}[language=bash, caption=Windows Installation Commands, label=lst:windows_installation_commands]
$ sudo apt update
$ sudo apt install yosys
$ sudo apt install nextpnr-ice40 
$ sudo apt install fpga-icestorm
\end{lstlisting}
}


%===============================================================
% Software : Verifying the Installations 
%===============================================================
\subsection{Verifying the Installations}
\label{sec:software:verifying_the_installations}

To verify that the tools have been installed correctly, we can use the Unix "which" command. If the tool is installed, running the "which" command will print the path to the executable. If not, command will print an error message saying the tool was not found.

Use the following commands to verify the necessary tools to generate and load a bitstream have been installed.

{
\vspace{0.6cm}
\begin{lstlisting}[language=bash, caption=Verify the Installation, label=lst:verfy_the_installation]
$ which yosys
$ which nextpnr-ice40
$ which icepack 
$ which iceprog 
\end{lstlisting}
}
-->

