# Mission 01 — Computer basics and IPOS

## 1. Task / objective

Explain how a computer takes input, processes it, produces output and stores results (IPOS); classify the hardware and software I actually use; and identify computer-based systems in everyday life other than a laptop or phone.

## 2. Work completed

### Task 1.1 — One activity traced through IPOS

**Activity chosen:** recording and sending a voice note on WhatsApp with a smartphone.

| Stage | What happens | Hardware / component |
|---|---|---|
| **Input** | I hold the mic icon and speak; sound waves reach the microphone and are converted to a digital signal, while the touchscreen registers the touch-and-hold. | Microphone, touchscreen |
| **Processing** | The phone filters background noise, balances the volume and compresses the raw audio into a smaller format that can be sent. | Mobile SoC (CPU / DSP) and RAM |
| **Output** | A live waveform and running timer appear on screen while recording; pressing play sends the audio to the speaker. | Display, speaker |
| **Storage** | Releasing the button saves the clip to internal storage and uploads a copy to the chat history in the cloud. | Internal flash storage, cloud storage |

**How the activity moves through the stages:** physical sound and touch become input, the processor and memory turn that input into a compressed file, the screen and speaker give immediate feedback as output, and the finished clip is written to internal and cloud storage so it can be played again later. All four stages overlap in real time rather than happening one after another.

### Task 1.2 — Hardware and software I use

| Item / software | Hardware or software? | Category / type | Purpose |
|---|---|---|---|
| **Apple Silicon SoC** | Hardware | Processor / graphics | Runs applications and handles graphics efficiently. |
| **Unified memory (RAM)** | Hardware | Memory | Holds running apps and open tabs so multitasking stays smooth. |
| **SSD** | Hardware | Permanent storage | Stores files and applications; keeps boot and launch times short. |
| **Trackpad** | Hardware | Input device | Scrolling, clicking and multi-finger navigation. |
| **Finder** | Software | Operating-system software (file manager) | Browses folders, previews files and moves data. |
| **Spotlight** | Software | Utility software | Launches apps, searches files and evaluates quick calculations. |
| **Google Chrome** | Software | Application software | Browsing the web and opening documents. |
| **Rectangle** | Software | Utility software | Tiles and snaps windows with keyboard shortcuts. |

### Task 1.3 — Computer-based systems around me

| System | Main purpose | One input | One output |
|---|---|---|---|
| **Smartwatch** | Tracks steps, heart rate and workouts and shows quick notifications. | Touchscreen or heart-rate sensor | Vibration or a screen alert on the wrist |
| **Smart TV** | Streams shows, films and videos on a living-room display. | Remote-control button press or voice command | Video and audio from the screen and speakers |
| **Wireless earbuds** | Plays music, podcasts and call audio with on-device controls. | Touch tap on the earbud stem | Audio played into the ear |

## 3. Commands / tools used

No Terminal commands were required for this mission. I observed the devices around me and recorded the answers in Markdown using a text editor.

| Tool | Purpose |
|---|---|
| Smartphone, laptop, smartwatch, smart TV, earbuds | Observed as real examples of input, processing, output and storage. |
| VS Code | Wrote the tables and explanations. |
| Git | Committed the completed mission. |

## 4. My understanding

Every computer, from a laptop to a smartwatch to an ATM, runs the same loop: something is captured as input, a processor works on it with the help of memory, a result is presented as output, and the data is kept for later. The loop is what makes them all "computers" even though their hardware looks nothing alike.

Hardware is the physical part; software is the instructions. Within software the split matters: operating-system software manages the machine and its resources (Finder), application software does a task for me (Chrome), and utility software maintains or assists the system (Spotlight, Rectangle). Splitting the everyday devices into these categories showed me that the categories are about *role*, not size.

## 5. Difficulties faced

- Separating **processing** from **output** in the voice-note example — noise filtering and compression happen inside the phone, while the waveform and sound are what I actually see and hear.
- Deciding whether Finder is application software or operating-system software, since it opens like an app but manages files for the OS.

## 6. How I resolved them

- I asked "is this something the device *does* to the data, or something it *shows* me?" — anything that transforms the data was placed under processing.
- I classified Finder as operating-system software because it is the standard file manager shipped with macOS and exposes the file system itself, not a task I chose to perform.

## 7. Evidence / files

- The three completed tables in this README (IPOS, hardware/software classification, everyday systems).

## 8. Commit details

Commit message: **Complete computer basics and IPOS mission**

Pushed to GitHub on the `main` branch and verified the README on the repository page.
