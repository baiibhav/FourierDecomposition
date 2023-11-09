import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Initialize the frequency and amplitude lists
frequencies = []
amplitudes = []

def update_wave_plot(val):
    num_sines = int(slider.val)

    # Update the number of sine waves display
    num_sines_display.set_text(str(num_sines))

    # Define the time range and the number of samples
    start_time = 0
    end_time = 2 * np.pi
    num_samples = 1000

    # Generate the time values
    t = np.linspace(start_time, end_time, num_samples)

    # Initialize the combined wave and individual sine waves
    combined_wave = np.zeros_like(t)
    sine_waves = [np.zeros_like(t) for _ in range(num_sines)]

    # Generate the individual sine waves and add them to the combined wave
    for i in range(num_sines):
        freq = 2 * i + 1  # Frequency of the sine wave
        amp = 4 / (np.pi * freq)  # Amplitude of the sine wave
        sine_wave = amp * np.sin(freq * t)
        sine_waves[i] = sine_wave
        combined_wave += sine_wave

    # Update the line data for the combined wave
    combined_line.set_data(t, combined_wave)

    # Update the line data for the individual sine waves
    for i, sine_line in enumerate(sine_lines):
        if i < num_sines:
            sine_line.set_data(t, sine_waves[i])  # Update the line data for the sine waves
        else:
            sine_line.set_data([], [])  # Clear the line data for the unused sine waves

    # Update the graph limits
    ax.relim()
    ax.autoscale_view()

    # Redraw the plot
    fig.canvas.draw_idle()

def add_sine_wave(event):
    # Increment the slider value by 1
    slider.set_val(slider.val + 1)

def remove_sine_wave(event):
    # Decrement the slider value by 1
    slider.set_val(slider.val - 1)

def reset_plot(event):
    # Reset the slider value and update the plot
    slider.reset()
    update_wave_plot(0)

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(10, 7))

# Create a line for the combined wave
combined_line, = ax.plot([], [], linewidth=2)

# Create lines for the individual sine waves
sine_lines = []
for _ in range(100):
    line, = ax.plot([], [])
    sine_lines.append(line)

# Create a slider widget for adjusting the number of input sine waves
slider_ax = plt.axes([0.15, 0.1, 0.7, 0.03])
slider = Slider(slider_ax, 'Number of Sines', 0, 100, valinit=0, valstep=1)

# Create a text display for the number of sine waves
num_sines_display = plt.text(0.85, 0.05, str(int(slider.val)), transform=ax.transAxes, fontsize=12)

# Update the wave plot when the slider value changes
slider.on_changed(update_wave_plot)

# Create a plus button
plus_ax = plt.axes([0.9, 0.1, 0.05, 0.03])
plus_button = Button(plus_ax, '+')

# Add a sine wave when the plus button
plus_button.on_clicked(add_sine_wave)

# Create a minus button
minus_ax = plt.axes([0.95, 0.1, 0.05, 0.03])
minus_button = Button(minus_ax, '-')

# Remove a sine wave when the minus button is clicked
minus_button.on_clicked(remove_sine_wave)

# Create a reset button
reset_ax = plt.axes([0.85, 0.02, 0.1, 0.04])
reset_button = Button(reset_ax, 'Reset', hovercolor='0.975')

# Reset the plot when the reset button is clicked
reset_button.on_clicked(reset_plot)

# Show the plot
plt.show()
