# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 15:59:14 2026

@author: samhl
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, PhotoImage
import random
import csv
from PIL import Image, ImageTk

# --- Laser-tag style names ---
ListNames = [
    "Raptor", "Blaze", "Phantom", "Vortex", "Shadow", "Striker", "Falcon", "Rogue",
    "Titan", "Bolt", "Knight", "Glitch", "Viper", "Echo", "Nova", "Inferno",
    "Specter", "Mirage", "Turbo", "Reaper", "Blitz", "Ranger", "Cypher", "Matrix",
    "Pulse", "Havoc", "Comet", "Jester", "Orbit", "Drift", "Sabre", "Howler",
    "Rumble", "Trigger", "Quake", "Hunter", "Gamma", "Delta", "Omega", "Fury",
    "Keenan", "Beasley",

    "Apex", "Zenith", "Onyx", "Atlas", "Neon", "Storm", "Crusher", "Wrath",
    "Spectra", "Volt", "Nebula", "Phaser", "Ignite", "Cinder", "Frost", "Arctic",
    "Blizzard", "Tempest", "Cyclone", "Talon", "Sonic", "Quasar", "Stellar", "Lynx",
    "Panther", "Jaguar", "Leopard", "Cobra", "Python", "Mamba", "Scorpion", "VortexX",
    "Darkstar", "Nightfall", "ShadowX", "Ironclad", "Steel", "TitanX", "Obsidian",
    "Granite", "Stone", "Rock", "Flare", "Spark", "Flash", "Glare", "Radiant",
    "Photon", "Laser", "Plasma", "Ion", "Vector", "Signal", "Codec", "Byte",

    "Core", "Sync", "EchoX", "PulseX", "NovaX", "InfernoX", "BlazeX", "RogueX",
    "FalconX", "ViperX", "RaptorX", "StrikerX", "KnightX", "PhantomX", "ReaperX",
    "HavocX", "FuryX", "OmegaX", "DeltaX", "GammaX", "Alpha", "Beta", "Sigma",
    "Theta", "Lambda", "Zeta", "Epsilon", "Kappa", "Iota", "Phi", "Psi",

    "BlitzX", "RangerX", "HunterX", "DriftX", "OrbitX", "CometX", "MatrixX",
    "CypherX", "TriggerX", "QuakeX", "RumbleX", "PulseZ", "NovaZ", "BlazeZ",
    "ShadowZ", "VortexZ", "TitanZ", "BoltZ", "EchoZ", "PhantomZ",

    "Iron", "SteelX", "Carbon", "Alloy", "Fusion", "Quantum", "Nexus", "Axis",
    "Prime", "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
    "Eight", "Nine", "Ten", "Zen", "Flux", "Drive", "Edge", "Shift",

    "Breaker", "Destroyer", "Annihilator", "Executioner", "Predator", "Sentinel",
    "Guardian", "Warden", "Patrol", "Recon", "Scout", "Infiltrator", "Operative",
    "Agent", "AgentX", "Unit", "UnitX", "Division", "Squad", "Force", "Tasker",

    "Arrow", "ArrowX", "Sniper", "Marksman", "Sharpshot", "Deadeye", "Longshot",
    "Quickshot", "Fastlane", "Speedster", "Dash", "Rush", "Sprint", "Charge",
    "Impact", "StrikeX", "ImpactX", "Shock", "Shockwave", "Overload",

    "BreakerX", "CrusherX", "Wrecker", "Smash", "Hammer", "Anvil", "Forge",
    "Blade", "EdgeX", "Cutlass", "SabreX", "Dagger", "Sting", "Piercer",
    "Thrasher", "Slayer", "Grim", "GrimX", "ReapX",

    "Cyber", "CyberX", "Neuro", "NeuroX", "Tech", "TechX", "Data", "DataX",
    "Grid", "Mesh", "Node", "NodeX", "Link", "Bridge", "Portal", "Gateway",

    "FlashX", "GlitchX", "PulseWave", "NovaWave", "StormX", "TempestX",
    "CycloneX", "BlizzardX", "ArcticX", "InfernoWave", "VoltX",

    "Aero", "AeroX", "Aether", "AetherX", "Void", "VoidX", "Dark", "DarkX",
    "Light", "LightX", "Star", "StarX", "Cosmo", "CosmoX", "Galaxy", "GalaxyX",

    "PhantomZ", "VortexZ", "ShadowZ", "BlazeZ", "RaptorZ", "FalconZ",
    "StrikerZ", "KnightZ", "TitanZ", "BoltZ", "EchoZ", "NovaZ",
    
    "Sunny", "Buddy", "Sparkle", "Pebble", "Rocket",
    "Bubbles", "Maple", "Skipper", "Doodle", "Ziggy",
    "Peanut", "Pogo", "Snappy", "Waffles", "Muffin",
    "Clover", "Pipsqueak", "Twinkle", "Jellybean", "Popcorn",
    "Skittles", "Sprout", "Marble", "Scoot", "Tinker"
    
]

global copy_icons, copy_colors, sequence_New
last_icon_prev_sequence = None

# This boolean is used to indicate that the current user is the first user 
firstUser = True
scores = []

# Initialize booleans to represent state of the gate
gate1 = gate2 = gate3 = False
 
# Initialize current user's score to 0
Current_User_Score = 0
firstRead = 0 
firstRun = True
firstGate = True 

# --- Shape + Color combos ---
#icons = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# This function draws a path
def generate_path_garrick():
    global sequence_New

    allowed_pairs = [(1, 1), (2, 3), (3, 2), (4,4)]

    # Pick 3 pairs, repeats allowed
    chosen = random.choices(allowed_pairs, k=3)

    # Separate into two aligned lists
    icons = [pair[0] for pair in chosen]
    colors = [pair[1] for pair in chosen]

    sequence_New = True
    return icons, colors


def generate_path():
    global last_icon_prev_sequence

    allowed_pairs = [(1, 1), (2, 3), (3, 2), (4,4)]

    icons = []
    colors = []

    # --- FIRST ITEM (with restriction) ---
    first_choices = allowed_pairs.copy()

    if last_icon_prev_sequence is not None:
        first_choices = [p for p in first_choices if p[0] != last_icon_prev_sequence]

    # Safety fallback (should rarely trigger)
    if not first_choices:
        first_choices = allowed_pairs.copy()

    first_pair = random.choice(first_choices)
    icons.append(first_pair[0])
    colors.append(first_pair[1])

    # --- REMAINING ITEMS (no repeats) ---
    remaining_pairs = [p for p in allowed_pairs if p != first_pair]

    for _ in range(2):  # need 2 more items to make 3 total
        pair = random.choice(remaining_pairs)
        icons.append(pair[0])
        colors.append(pair[1])
        remaining_pairs.remove(pair)

    # --- Update memory for next call ---
    last_icon_prev_sequence = icons[-1]

    return icons, colors


def show_penalty_x(canvas, duration_ms=3000):
    canvas.update_idletasks()

    w = canvas.winfo_width()
    h = canvas.winfo_height()

    x1 = canvas.create_line(20+470, 20, 470-20, h-20, fill="red", width=6)
    x2 = canvas.create_line(20+470, h-20, 470-20, 20, fill="red", width=6)

    #x3 = canvas.create_line(20+420, 20, 420-20, h-20, fill = "red", width=6)
    #x4 = canvas.create_line(20+420, h-20, 420-20, 20, fill = "red", width=6)
    
    canvas.after(duration_ms, lambda: (
        canvas.delete(x1),
        canvas.delete(x2)
        #canvas.delete(x3)
        #canvas.delete(x4)
    ))

def show_success_x(canvas, duration_ms=3000):
    canvas.update_idletasks()
    w = canvas.winfo_width()
    h = canvas.winfo_height()

    # Draw checkmark using two lines
    check1 = canvas.create_line(w//2 - 30 - 300, h//2,
                                 w//2 - 10 - 300, h//2 + 20,
                                 fill="green", width=6)
    check2 = canvas.create_line(w//2 - 10 - 300, h//2 + 20,
                                 w//2 + 30 - 300, h//2 - 20,
                                 fill="green", width=6)

    canvas.after(duration_ms, lambda: (
        canvas.delete(check1),
        canvas.delete(check2)
    ))
    
# --- Timer Class ---
class TwoMinuteTimer(ttk.Frame):
    def __init__(self, master, minutes=1, score_var=None, top_scores=None, update_scoreboard=None, current_user_var=None, **kwargs):
        super().__init__(master, **kwargs)
        self.total_seconds = minutes * 60
        self.remaining = self.total_seconds
        self._running = False
        self._after_id = None

        # References for updating scoreboard and current user
        self.score_var = score_var
        self.top_scores = top_scores
        self.update_scoreboard = update_scoreboard
        self.current_user_var = current_user_var

        self.time_var = tk.StringVar(value=self._format_time(self.remaining))
        ttk.Label(self, textvariable=self.time_var, font=("TkDefaultFont", 32)).grid(
            row=0, column=0, columnspan=3, pady=(0, 12)
        )

        self.progress = ttk.Progressbar(self, maximum=self.total_seconds, length=240)
        self.progress.grid(row=1, column=0, columnspan=3, pady=(10, 0))

    def _format_time(self, secs: int) -> str:
        mins, s = divmod(secs, 60)
        return f"{mins:02}:{s:02}"

    def _tick(self):
        if not self._running:
            return
        if self.remaining <= 0:
            self._finish()
            return
        self.remaining -= 1
        self.time_var.set(self._format_time(self.remaining))
        self.progress['value'] = self.total_seconds - self.remaining
        self._after_id = self.after(1000, self._tick)

    def start(self):
        if self._running:
            return
        self._running = True
        if self.remaining <= 0:
            self.remaining = self.total_seconds
            self.progress['value'] = 0

        self._after_id = self.after(1000, self._tick)

    def reset(self):
        if self._after_id:
            self.after_cancel(self._after_id)
        self._running = False
        self.remaining = self.total_seconds
        self.time_var.set(self._format_time(self.remaining))
        self.progress['value'] = 0
        
    def add_time(self, extra_seconds):
        """Add time to the remaining countdown."""
        self.remaining += extra_seconds
        if self.remaining > self.total_seconds:
            self.remaining = self.total_seconds  # Optional: cap at max time
        self.time_var.set(self._format_time(self.remaining))
        self.progress['value'] = self.total_seconds - self.remaining
    
    def _finish(self):
        self._running = False
        self.time_var.set("00:00")
        self.progress['value'] = self.total_seconds

        # --- Generate a new path ---
        new_path = generate_path()
        draw_path(new_path)

        # --- Update top 10 scores ---
        try:
            score = int(self.score_var.get())
        except (ValueError, TypeError):
            score = 0

        if score > 0 and self.top_scores is not None:
            # find lowest score
            min_index = min(range(len(self.top_scores)), key=lambda i: self.top_scores[i][1])
            if score > self.top_scores[min_index][1]:
                new_name = random.choice(ListNames)
                self.top_scores[min_index] = (new_name, score)
                if self.update_scoreboard:
                    self.update_scoreboard()

# --- Main App ---
def main():       
    import tkinter as tk
    try:
        if tk._default_root:
            tk._default_root.destroy()
    except:
        pass
    
    global timer
    global firstTrigger
    global firstGate
    time_boost_used = False
    power_up2_used = False 
    firstRun = True
    
    root = tk.Tk()
    root.title("External Trigger Timer")
    root.geometry("600x600")
      
    banana_img = PhotoImage(file="BannanaPeel.png")
    
    #canvasBannanaPeel = Canvas(root, width=400, height=300)
    #canvasBannanaPeel.pack()
    
    # Load image
    #img = PhotoImage(file="BannanaPeel.png")
    
    # Place image (top-left corner)
   #canvasBannanaPeel.create_image(0, 0, anchor="nw", image=img)

    #canvasBannanaPeel.image = img
    
    main_frame = ttk.Frame(root)
    main_frame.pack(expand=True, fill="both", padx=20, pady=20)

    # --- Top 10 Scores Data ---
    top_scores = [(f"Player{i}", 0) for i in range(1, 11)]

    # WIDGET for the current user's name
    current_user_var = tk.StringVar(value="Waiting for start...")
    '''ttk.Label(main_frame, text="Current User:", font=("TkDefaultFont", 14, "bold")).grid(row=4, column=0, columnspan=2)
    ttk.Label(main_frame, textvariable=current_user_var, font=("TkDefaultFont", 16)).grid(row=5, column=0, columnspan=2, pady=(0,5))'''
    
    ttk.Label(main_frame, text="Current User:", font=("TkDefaultFont", 14, "bold")).grid(row=4, column=1, sticky="", padx=(0,120))
    ttk.Label(main_frame, textvariable=current_user_var, font=("TkDefaultFont", 16)).grid(row=5, column=1, pady=(0,5), padx=(0,120), sticky="")

    # Top 10 Scores title
    # --- Top 10 Scores UI ---
    #ttk.Label(main_frame, text="Top 10 Scores", font=("TkDefaultFont", 16, "bold")).grid(row=6, column=0, columnspan=2, pady=(10, 5))
    ttk.Label(main_frame, text="Top 10 Scores", font=("TkDefaultFont", 16, "bold")).grid(row=6, column=1, pady=(10, 5), padx=(0,120), sticky="")
    
    scores_frame = ttk.Frame(main_frame)
    scores_frame.grid(row=7, column=1, sticky="", pady=(10, 0), padx=(0,120))
    #scores_frame.grid(row=7, column=1, columnspan=2)

    left_col = ttk.Frame(scores_frame)
    right_col = ttk.Frame(scores_frame)
    left_col.grid(row=0, column=0, padx=5)
    right_col.grid(row=0, column=1, padx=5)

    left_labels = []
    right_labels = []

    for i in range(5):
        lbl = ttk.Label(left_col, text=f"{i+1}. __________", font=("TkDefaultFont", 12))
        lbl.pack(anchor="w")
        left_labels.append(lbl)

    for i in range(5):
        lbl = ttk.Label(right_col, text=f"{i+6}. __________", font=("TkDefaultFont", 12))
        lbl.pack(anchor="w")
        right_labels.append(lbl)

    # --- Score Display ---
    score_var = tk.StringVar(value="0")
    timer = TwoMinuteTimer(
        main_frame,
        minutes=1,
        score_var=score_var,
        top_scores=top_scores,
        current_user_var=current_user_var
    )
    timer.grid(row=0, column=0, sticky="nsew", padx=(0, 20))

    score_frame = ttk.Frame(main_frame)
    score_frame.grid(row=0, column=2, sticky="n")
    ttk.Label(score_frame, text="Score:", font=("TkDefaultFont", 20)).pack(anchor="center")
    ttk.Label(score_frame, textvariable=score_var, font=("TkDefaultFont", 28, "bold")).pack(anchor="center")

    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)
    
    TARGET_SIZE = (75, 75)  # Set whatever size you want here

    images_frame = ttk.Frame(main_frame)
    images_frame.grid(row=1, column=0, columnspan=3, pady=(10, 0))

    banana_img = Image.open("BannanaPeel.png").resize(TARGET_SIZE, Image.LANCZOS)
    banana_img = ImageTk.PhotoImage(banana_img)
    banana_label = tk.Label(images_frame, image=banana_img)
    banana_label.image = banana_img
    banana_label.pack(side="left", padx=5)
    
    mysteryBox_img = Image.open("MysteryBox.png").resize(TARGET_SIZE, Image.LANCZOS)
    mysteryBox_img = ImageTk.PhotoImage(mysteryBox_img)
    mysteryBox_label = tk.Label(images_frame, image=mysteryBox_img)
    mysteryBox_label.image = mysteryBox_img
    mysteryBox_label.pack(side="left", padx=5)
    
    marioKart_img = Image.open("MarioKart.png").resize(TARGET_SIZE, Image.LANCZOS)
    marioKart_img = ImageTk.PhotoImage(marioKart_img)
    marioKart_label = tk.Label(images_frame, image=marioKart_img)
    marioKart_label.image = marioKart_img
    marioKart_label.pack(side="left", padx=5)
    
    Bowser_img = Image.open("Bowser.png").resize(TARGET_SIZE, Image.LANCZOS) 
    Bowser_img = ImageTk.PhotoImage(Bowser_img) 
    Bowser_label = tk.Label(images_frame, image=Bowser_img) 
    Bowser_label.image = Bowser_img 
    Bowser_label.pack(side="left", padx=5) 
    
    Mushroom_img = Image.open("Mushroom.png").resize(TARGET_SIZE, Image.LANCZOS) 
    Mushroom_img = ImageTk.PhotoImage(Mushroom_img) 
    Mushroom_label = tk.Label(images_frame, image=Mushroom_img) 
    Mushroom_label.image = Mushroom_img 
    Mushroom_label.pack(side="left", padx=5) 
    
    shell_img = Image.open("shell.png").resize(TARGET_SIZE, Image.LANCZOS) 
    shell_img = ImageTk.PhotoImage(shell_img) 
    shell_label = tk.Label(images_frame, image=shell_img) 
    shell_label.image = shell_img 
    shell_label.pack(side="left", padx=5)
    
    text_label = tk.Label(
    root,
    text="E-Day Drive",
    font=("Times New Roman", 50),
    fg="blue"
    )
    text_label.pack(pady=10)

    TRACK_SIZE = (200,200)
    bottom_left_frame = ttk.Frame(main_frame)
    bottom_left_frame.grid(row=7, column=0, sticky="sw", pady=(10, 0))
    
    bottom_right_frame = ttk.Frame(main_frame)
    bottom_right_frame.grid(row=7, column=2, sticky="sw", pady=(10, 0))
    
    RainbowRoad_img = Image.open("RainbowRoad.png").resize(TRACK_SIZE, Image.LANCZOS)
    RainbowRoad_img = ImageTk.PhotoImage(RainbowRoad_img)
    RainbowRoad_label = tk.Label(bottom_left_frame, image=RainbowRoad_img)
    RainbowRoad_label.image = RainbowRoad_img
    RainbowRoad_label.pack(side="left", padx=5)
    
    MarioCircuit_img = Image.open("MarioCircuit.png").resize(TRACK_SIZE, Image.LANCZOS)
    MarioCircuit_img = ImageTk.PhotoImage(MarioCircuit_img)
    MarioCircuit_label = tk.Label(bottom_left_frame, image=MarioCircuit_img)
    MarioCircuit_label.image = MarioCircuit_img
    MarioCircuit_label.pack(side="left", padx=5)
    
    #DonutPlains_img = Image.open("DonutPlains.png").resize(TRACK_SIZE, Image.LANCZOS)
    #DonutPlains_img = ImageTk.PhotoImage(DonutPlains_img)
    #DonutPlains_img = tk.Label(bottom_right_frame, image=DonutPlains_img)
    #DonutPlains_label.image = DonutPlains_img
    #DonutPlains_label.pack(side="left", padx=5)
    
    '''DonutPlains_img = Image.open("DonutPlains.png").resize(TRACK_SIZE, Image.LANCZOS)
    DonutPlains_img = ImageTk.PhotoImage(DonutPlains_img)
    DonutPlains_label = tk.Label(bottom_right_frame, image=DonutPlains_img)
    DonutPlains_label.image = DonutPlains_img  # keep reference!
    DonutPlains_label.pack(side="left", padx=5)

    BowsersCastle_img = Image.open("BowsersCastle.png").resize(TRACK_SIZE, Image.LANCZOS)
    BowsersCastle_img = ImageTk.PhotoImage(BowsersCastle_img)
    BowsersCastle_img = tk.Label(bottom_right_frame, image = BowsersCastle_img)
    BowsersCastle_label.image = BowsersCastle_img
    BowsersCastle_label.pack(side="left", padx=5)
    
    BowsersCastle_img = Image.open("BowsersCastle.png").resize(TRACK_SIZE, Image.LANCZOS)
    BowsersCastle_img = ImageTk.PhotoImage(BowsersCastle_img)
    BowsersCastle_label = tk.Label(bottom_right_frame, image=BowsersCastle_img)
    BowsersCastle_label.image = BowsersCastle_img  # keep reference
    BowsersCastle_label.pack(side="left", padx=5)'''
    
    DonutPlains_img = Image.open("DonutPlains.png").resize(TRACK_SIZE, Image.LANCZOS)
    DonutPlains_photo = ImageTk.PhotoImage(DonutPlains_img)
    DonutPlains_label = tk.Label(bottom_right_frame, image=DonutPlains_photo)
    DonutPlains_label.image = DonutPlains_photo
    DonutPlains_label.pack(side="left", padx=5)
    
    BowsersCastle_img = Image.open("BowsersCastle.png").resize(TRACK_SIZE, Image.LANCZOS)
    BowsersCastle_photo = ImageTk.PhotoImage(BowsersCastle_img)
    BowsersCastle_label = tk.Label(bottom_right_frame, image=BowsersCastle_photo)
    BowsersCastle_label.image = BowsersCastle_photo
    BowsersCastle_label.pack(side="left", padx=5)
    
    # --- PATH CANVAS ---
    global draw_path
    path_canvas = tk.Canvas(main_frame, height=120, bg="white",
                            highlightthickness=1, highlightbackground="#ccc")
    path_canvas.grid(row=2, column=0, columnspan=3, pady=(5, 10), sticky="ew")

        # --- TOP CANVAS ---
    top_canvas = tk.Canvas(
        main_frame,
        height=120,
        bg="white",
        highlightthickness=1,
        highlightbackground="#ccc"
    )
    top_canvas.grid(row=3, column=0, columnspan=3, pady=0, sticky="ew")
    

    # This is the function that draws the path of shapes
    # path is a tuple, first term represents the shape, the second term represents if it needs to be "grayed" out
    def draw_path(icons, colors):
        
        print_icons = icons
        print_colors = colors
        
        for i, icon in enumerate(icons):
            if icon == 1:
                print_icons[i] = "square"
            elif icon == 2:
                print_icons[i] = "triangle"
            elif icon == 3:
                print_icons[i] = "half-circle"
            elif icon == 4:
                print_icons[i] = "oval"
                
        for i, color in enumerate(colors):
            if color == 0:
                print_colors[i] = "gray"
            elif color == 1:
                print_colors[i] = "blue"
            elif color == 2:
                print_colors[i] = "yellow"
            elif color == 3:
                print_colors[i] = "orange"
            elif color == 4:
                print_colors[i] = "purple"
        
        print_path = list(zip(print_icons, print_colors))
        
        
        path_canvas.delete("all")
        x_offset = 600
        y_center = 60
        size = 50
        for shape, color in print_path:
            if shape == "square":
                path_canvas.create_rectangle(x_offset-size/2, y_center-size/2,
                                             x_offset+size/2, y_center+size/2,
                                             fill=color, outline="black")
            elif shape == "triangle":
                path_canvas.create_polygon(x_offset, y_center-size/2,
                                           x_offset-size/2, y_center+size/2,
                                           x_offset+size/2, y_center+size/2,
                                           fill=color, outline="black")
            elif shape == "half-circle":
                path_canvas.create_arc(x_offset-size/2, y_center-size/2,
                                       x_offset+size/2, y_center+size/2,
                                       start=0, extent=180, fill=color, outline="black")
            elif shape == "oval":
                print("Keenan")
                path_canvas.create_oval(x_offset-size/2, y_center-size,
                            x_offset+size/2, y_center+size,
                            fill=color, outline="black")
                
            x_offset += 140
        return icons, colors
    
    # This is a helper function for insert_into_top10      
    def update_top10_labels(top_scores, left_labels, right_labels):
        """
        Update the Tkinter labels to show the top 10 scores.
    
        top_scores: list of tuples (username, score) sorted descending
        left_labels: list of 5 labels for positions 1–5
        right_labels: list of 5 labels for positions 6–10
        """

        # Fill in left column (1–5)
        for i in range(5):
            if i < len(top_scores):
                name, score = top_scores[i]
                left_labels[i].config(text=f"{i+1}. {name} - {score}")
            else:
                left_labels[i].config(text=f"{i+1}. __________")
    
        # Fill in right column (6–10)
        for i in range(5, 10):
            if i < len(top_scores):
                name, score = top_scores[i]
                right_labels[i-5].config(text=f"{i+1}. {name} - {score}")
            else:
                right_labels[i-5].config(text=f"{i+1}. __________")
  
        
    # This function takes the current setof scores, the curent user's score and username, and 
    # updates the scoreboard
    def insert_into_top10(all_scores, username, current_score):
        """
        all_scores: list of (username, score)
        username: string
        current_score: int
    
        Returns:
            rating (1–10) if placed in Top 10
            None if not placed
        """

        # Add the new score
        all_scores.append((username, current_score))
    
        # Sort by score descending
        all_scores.sort(key=lambda x: x[1], reverse=True)
    
        # Trim to top 10 only
        if len(all_scores) > 10:
            all_scores[:] = all_scores[:10]
    
        update_top10_labels(all_scores, left_labels, right_labels)
        
        return None  # Did not make Top 10

    def updateGates(icons, colors):
        global firstRead, sequence_New, path, Current_User_Score, copy_icons, copy_colors
        global signalTriggered, gateTriggered, overrideTriggered
        # The input for this function is icons, and colors
        # these are each arrays of 3 
        # each value in icons correpsonds to the shape in the sequence
        # each value in colors corresponds to the color of the shape in the sequence 
        
        # Will read CSV and process booleans
        # if signal triggered, that boolean will turn true
        # if a gate is triggered, the GUI will update
        # Step 2.) Read in CSV File (Garrick)
        
        with open("Garrick.csv", newline = '') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                a, b, c = map(int, row)  # convert CSV strings to integers
                #print(a, b, c)
        
        if firstRead == 0:
            signalTriggered_diff = a
            gateTriggered_diff = b
            override_diff = c
            firstRead = 1
        else:
            signalTriggered_diff = a - signalTriggered
            gateTriggered_diff = b - gateTriggered
            override_diff = c - overrideTriggered

        # update previous values
        signalTriggered = a
        gateTriggered = b
        overrideTriggered = c
        
        print(signalTriggered_diff, gateTriggered_diff, override_diff)
        
        # 3.) Check if the "Reset" button has been pressed, if it has then reset the GUI
        if signalTriggered_diff == 1:
            check_external_signal()
        
        # Original path is used to for drawing
        # copy of the path is used for determining if the correct gate was driven through
        # 4.) Create a copy of icons and colors, these are going to be used for the comparison to check if the current gate in the sequence 
        # driven through
        # We only copy the sequence of icons/shapes 
            
        # 5.) Check if the override button was pressed:
        if override_diff == 1:
            # then we add + 5 points, and then make the color gray
            # Adds 5 to user's score, # Change to next gate in the sequence
            if len(icons) == 3:
                Current_User_Score += 5
                score_var.set(Current_User_Score)
            elif len(icons) == 2:
                Current_User_Score += 10 
                score_var.set(Current_User_Score)
            elif len(icons) == 1:
                Current_User_Score += 153
                score_var.set(Current_User_Score)
                
            icons.pop(0)
            colors.pop(0)
             
            if len(icons) == 0:
               icons, colors = draw_path(*generate_path())
            else:
                 draw_path(icons, colors) # Redraw shapes
                 
        elif override_diff == 2:
            timer.add_time(10) # Time boost power up
          
        
        # 5.) Check if one of the gates has been driven through
        # gateTriggered = 0 means that no gate has been driven through
        if gateTriggered_diff != 0:
            gate = gateTriggered_diff
            
            # initialize to None by default
            gate_shape = None
            gate_color = None
            
            # If a gate is driven through, then we first need to convert the 1-9 to shape 1-3 and color 1-3
            # the variables
            
            if gate == 1: # gate 1 = Blue Square
                gate_shape = "square" #1
                gate_color = "blue"   #1
            elif gate == 2: # gate 2 = yellow Half-Circle
                gate_shape = "half-circle" #1
                gate_color = "yellow" #2
            elif gate == 3: # gate 3 = Orange Triangle
                gate_shape = "triangle" #1
                gate_color = "orange" #3
            elif gate == 4:  # gate 4 = Purple Oval
                gate_shape = "oval"   #4
                gate_color = "purple" #4 
                
            # If the gate is not a "regular" gate, then it's a power-up gate
            if gate == 5: # Time-Boost
                global time_boost_used
                if not time_boost_used: 
                    timer.add_time(10) # add 10 seconds to time
                    time_boost_used = True
                    
            if gate == 6: # Time-boost or +7 points
                global power_up2_used
                if not power_up2_used:
                    num = random.choice([1,2])
                    if num == 1:
                        timer.add_time(10)
                    elif num == 2:
                        Current_User_Score += 7
                        score_var.set(Current_User_Score)
                        
                    power_up2_used = True
                    
            #print(icons[0], colors[0])
            # Check if the current gate in the sequence has been driven through 
            if gate_shape is not None and gate_color is not None:
                if gate_shape == icons[0] and gate_color == colors[0]:
                    
                    # then we add + 5 points, and then make the color gray
                    # Adds 5 to user's score
                    if len(icons) == 3:                       
                        Current_User_Score += 5
                        score_var.set(Current_User_Score)
                    elif len(icons) == 2:
                        Current_User_Score += 10 
                        score_var.set(Current_User_Score)
                    elif len(icons) == 1:
                        Current_User_Score += 15
                        score_var.set(Current_User_Score)
                        
                    print("pathgary")
                    print(colors)
                    
                    icons.pop(0)
                    colors.pop(0)
                    
                    if len(icons) == 0:
                      icons, colors = draw_path(*generate_path())
                    else:
                        draw_path(icons, colors) # Redraw shapes
                    
                    show_success_x(path_canvas, duration_ms=3000)
                    
                else:
                    Current_User_Score -= 2
                    score_var.set(Current_User_Score)
                    show_penalty_x(path_canvas, duration_ms=3000)
                
        root.after(500, lambda: updateGates(icons, colors))
    
    
    
    def check_external_signal():
        global Current_User_Score, firstUser, Current_Name, timer, firstRun, signalTriggered
        global icons, colors, time_boost_used, power_up2_used
    
        time_boost_used = False
        power_up2_used = False
    
        print("Starting Reset Loop")
    
        def wait_for_start_signal():
            global firstRun, signalTriggered
    
            with open("Garrick.csv", newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    a, b, c = map(int, row)
    
            if firstRun:
                if a == 0:
                    # Not triggered yet — check again in 200ms instead of blocking
                    root.after(200, wait_for_start_signal)
                    return
                else:
                    firstRun = False
            
            # Signal received — proceed with the rest of the setup
            _on_signal_received()
    
        def _on_signal_received():
            global Current_User_Score, firstUser, Current_Name, icons, colors, signalTriggered, firstGate
    
            print("No more Will Thompson")
    
            if not firstUser:
                insert_into_top10(scores, Current_Name, Current_User_Score)
    
            firstUser = False
            Current_User_Score = 0
            score_var.set(Current_User_Score)
    
            Current_Name = random.choice(ListNames)
            ListNames.remove(Current_Name)
            current_user_var.set(Current_Name)
    
            icons, colors = generate_path()
            draw_path(icons, colors)
    
            print("Path printed")
            print("Crickets")
            timer.reset()
            timer.start()
    
            if firstGate:
                updateGates(icons, colors)
    
            root.after(22100000, check_external_signal)
    
        wait_for_start_signal()
        
    def draw_checkerboard(canvas, rows, cols, size):
        colors = ["white", "black"]
    
        for row in range(rows):
            for col in range(cols):
                x1 = col * size
                y1 = row * size
                x2 = x1 + size
                y2 = y1 + size
    
                color = colors[(row + col) % 2]
    
                canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)      
            
    #draw_checkerboard(top_canvas, rows=8, cols=200, size=50)
    root.after(100, lambda: draw_checkerboard(top_canvas, rows=8, cols=200, size=50))
    root.after(1000, check_external_signal)
    root.mainloop()


if __name__ == "__main__":
    main()

