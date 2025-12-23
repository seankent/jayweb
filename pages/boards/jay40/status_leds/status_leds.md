# Status LEDs 


![Alt text](diag/jay40_pinout.svg){: style="width: 30rem;"}



<!--

%===============================================================
% LEDs 
%===============================================================
\newpage
\section{LEDs}
\label{sec:leds}

%===============================================================
% LEDs : Overview
%===============================================================
\subsection{Overview}
\label{sec:leds:overview}

The Jay40 is outfitted with two status LEDs, labeled \texttt{PWR} and \texttt{TEST}. The \texttt{PWR} LED is driven by the 3.3 V power rail and indicates the board is receiving power. The \texttt{TEST} LED is connected to the \texttt{D16} pin, which is driven by one of the FPGA programmable I/Os. Its function is left up to the user.


%\uselengthunit{mm}
%Text width: \printlength{\textwidth}

%Page width: \printlength{\paperwidth}

\begin{figure}[H]
    \centering
    %\includegraphics[width=\textwidth]{../../diag/export/jay40_led_highlight.pdf}
    \vspace{0.6cm}
    \includegraphics[width=12cm]{../../diag/export/jay40_led_highlight.pdf}
    \vspace{0.6cm}
    \caption{LED Locations}
    \label{fig:jay40_led_highlight}
\end{figure}

%\begin{figure}[H]
%    \vspace{0.6cm}
%    \centering
%    \begin{subfigure}{0.3\textwidth}
%        \centering
%        \uselengthunit{mm}
%        Text width: \printlength{\textwidth}
%        Page width: \printlength{\paperwidth}
%        \includegraphics[width=\textwidth]{../../diag/export/jay40_led_highlight.pdf}
%    \end{subfigure}
%    %\hfill
%    \hspace{0.6cm}
%    \begin{subfigure}{0.3\textwidth}
%        \centering
%        \includegraphics[width=\textwidth]{../../diag/export/jay40_led_cutout.pdf}
%    \end{subfigure}
%    \caption{LED Locations}
%    \label{fig:led_locations}
%\end{figure}

%\uselengthunit{mm}
%Text width: \printlength{\textwidth}
%Page width: \printlength{\paperwidth}

%\begin{figure}[H]
%    \vspace{0.6cm}
%    \centering
%%\uselengthunit{mm}
%%Text width: \printlength{\textwidth}
%%Page width: \printlength{\paperwidth}
%    \begin{subfigure}{0.49\textwidth}
%        \centering
%        \includegraphics[width=\textwidth]{../../diag/export/jay40_led_en_cutout_disconnected.pdf}
%        \caption{LEDs Connected}
%        \label{fig:leds_connected}
%    \end{subfigure}
%    %\hfill
%    \begin{subfigure}{0.49\textwidth}
%        \centering
%        \includegraphics[width=\textwidth]{../../diag/export/jay40_led_en_cutout_disconnected.pdf}
%        \caption{LEDs Disconnected}
%        \label{fig:leds_disconnected}
%    \end{subfigure}
%    \caption{LED EN Options}
%    \label{fig:led_locations}
%\end{figure}


%===============================================================
% LEDs : Disconnecting the LEDs 
%===============================================================
\subsection{Disconnecting the LEDs}
\label{sec:leds:disconnecting_the_leds}

Each LED consumes approximately 4 mA when illuminated. While it can be useful to have status LEDs when prototyping, the additional current draw may be undesirable in power constrained applications. To conserve power, the board provides a mechanism to disconnect the LEDs from their drivers. This is done using the two jumpers located next to the USB-C connector. When the jumpers are in place, the \texttt{PWR} and \texttt{TEST} LEDs are connected to their respective drivers. This configuration is shown in \autoref{fig:jay40_led_en_cutout_connected}. When the jumpers are removed, the LEDs are disconnected. This is shown in \autoref{fig:jay40_led_en_cutout_disconnected}. Each LED can be connected or disconnected independently of one another. 

\begin{figure}[H]
    \centering
    \begin{minipage}{0.68\textwidth}
        \centering
        \includegraphics[width=10cm]{../../diag/export/jay40_led_en_highlight.pdf}
        \caption{\texttt{LED EN} Location}
        \label{fig:jay40_led_en_highlight}
    \end{minipage}
    \hfill
    \begin{minipage}{0.3\textwidth}
        \centering
        \includegraphics[width=4cm]{../../diag/export/jay40_led_en_cutout_disconnected.pdf}
        \caption{LEDs Disconnected}
        \label{fig:jay40_led_en_cutout_disconnected}

        \vspace{0.5cm}

        \includegraphics[width=4cm]{../../diag/export/jay40_led_en_cutout_connected.pdf}
        \caption{LEDs Connected}
        \label{fig:jay40_led_en_cutout_connected}
    \end{minipage}
\end{figure}

%\begin{figure}[H]
%    \centering
%    \begin{minipage}{0.3\textwidth}
%        \centering
%        \includegraphics[width=4cm]{../../diag/export/jay40_led_en_cutout_disconnected.pdf}
%        \caption{First small figure}
%        \label{fig:small1}
%
%        \vspace{0.5cm}
%
%        \includegraphics[width=4cm]{../../diag/export/jay40_led_en_cutout_disconnected.pdf}
%        \caption{Second small figure}
%        \label{fig:small2}
%    \end{minipage}
%    \hfill
%    \begin{minipage}{0.68\textwidth}
%        \centering
%        \includegraphics[width=10cm]{../../diag/export/jay40_led_en_highlight.pdf}
%        \caption{Large figure}
%        \label{fig:large}
%    \end{minipage}
%\end{figure}



\autoref{fig:jay40_led_circuit} shows the driver circuit for the \texttt{PWR} and \texttt{TEST} LEDs.

\begin{figure}[H]
    \vspace{0.6cm}
    \centering
    \includegraphics[width=6cm]{../../diag/export/jay40_led_circuit.pdf}
    \caption{LED Circuit Diagram}
    \label{fig:jay40_led_circuit}
\end{figure}

-->
