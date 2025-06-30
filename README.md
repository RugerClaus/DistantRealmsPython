<h1>Welcome To The Distant Realms Framework/Engine-thingy</h1>



<b><p>This is a major work in progress, but currently has some features listed below</p></b>

<p>Robust state management and state driven workflows using a network of SRP Finite State Machines managing high to low level states in a hierarchy that is shaping to be many layers deep</p>

<p>An active input buffer via the cheeky <b>IOSTREAM</b> class in core.guts.input</p>

<p>The start of a strong debugging system with a debug overlay being accessible at any point in the program. Based on the Appstate, some information may be available/unavailable including context specific states like scenes. There are multiple commands that are detailed at the bottom of this file. The debugger has a system that I may make a toggle for where it displays every active character typed in the last 1000 milliseconds. This can make typing commands easier.</p>

<p>Abstraction of core Pygame functionality including rendering using the <b>Window</b> class. It can handle making surfaces removing the necessity of touching pygame's rendering logic at any other point in the program. This insists on abstracting the entire program into two fundamental application layer objects: <b>Window</b> and <b>App</b>. This is the highest level of the program. </p>

<p>Abstraction of the majority of Pygame's miniscule audio functionality to play music during game-play. Likely will need to be rewritten as an actual audio engine using some cpython module for audio.. PyOpenAL? The audio contains the included assets of original music. </p>
 
<p>I have begun the construction of a hopefully robust entity managment system. Entities are defined as any tile, character, or otherwise defined sprite or set of sprites on the screen. This includes NPCs such as hostile mobs and passive mobs. The system is being built with more than one possible player in mind. So all players even if there is only one are entities. All damaging tiles or tiles that have functionality at all will be entities, but not all tiles are entities. This is an important point, and a possible limitation. This is based on a previous implementation and i'm pretty far from re-implementing it in this project, so that will probably change based on the state system's requirements.</p>

<p>Currently there is no menu option adjustment for sound settings. I will likely add access to it from both the pause menu and the main menu, and probably at some point from the multiplayer system depending on how I handle that.</p>

<h2>Commands</h2>

<p>All commands can be typed as a key sequence at any point in the program. Whether you're at the main menu, in game, paused, or otherwise using the application, you can type any of these command sequences. Every character is literal. If there is a space in one of these commands, you will type the space when using that function. You can modify this via the <i>sequences</i> member of the <b>IOSTREAM</b> class.</p>

<p><b>DEBUG</b> - Toggles the debug overlay</p>

<p><b>SECRET</b> - Displays a secret message in the console</p>

<p><b>MUSICON</b> - Activates a random track and will change to another if typed while music is active</p>

<p><b>MUSICOFF</b> - Turns all music in the application off</p>

# this is for testing purposes ;)

<p><b>FUCK</b> - toggles a small red square that could be used for another type of debugging menu/functionality</p>

<p>Overall, this project is mainly applying concepts I've learned in abstracting SDL2 myself in using C++. Completely unnecessary given Pygame's intended user, but I'm building systems here god damnit!</p>