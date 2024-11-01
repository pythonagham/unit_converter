import tkinter as tk
from tkinter import ttk

# Conversion dictionaries
conversion_factors = {
    'Length': {
        'Meters': {'Meters': 1, 'Kilometers': 0.001, 'Miles': 0.000621371, 'Inches': 39.3701, 'Feet': 3.28084, 'Yards': 1.09361, 'Centimeters': 100, 'Millimeters': 1000},
        'Kilometers': {'Meters': 1000, 'Kilometers': 1, 'Miles': 0.621371, 'Inches': 39370.1, 'Feet': 3280.84, 'Yards': 1093.61, 'Centimeters': 100000, 'Millimeters': 1000000},
        'Miles': {'Meters': 1609.34, 'Kilometers': 1.60934, 'Miles': 1, 'Inches': 63360, 'Feet': 5280, 'Yards': 1760, 'Centimeters': 160934, 'Millimeters': 1609340},
        'Inches': {'Meters': 0.0254, 'Kilometers': 0.0000254, 'Miles': 0.0000157828, 'Inches': 1, 'Feet': 0.0833333, 'Yards': 0.0277778, 'Centimeters': 2.54, 'Millimeters': 25.4},
        'Feet': {'Meters': 0.3048, 'Kilometers': 0.0003048, 'Miles': 0.000189394, 'Inches': 12, 'Feet': 1, 'Yards': 0.333333, 'Centimeters': 30.48, 'Millimeters': 304.8},
        'Yards': {'Meters': 0.9144, 'Kilometers': 0.0009144, 'Miles': 0.000568182, 'Inches': 36, 'Feet': 3, 'Yards': 1, 'Centimeters': 91.44, 'Millimeters': 914.4},
        'Centimeters': {'Meters': 0.01, 'Kilometers': 0.00001, 'Miles': 0.00000621371, 'Inches': 0.393701, 'Feet': 0.0328084, 'Yards': 0.0109361, 'Centimeters': 1, 'Millimeters': 10},
        'Millimeters': {'Meters': 0.001, 'Kilometers': 0.000001, 'Miles': 0.000000621371, 'Inches': 0.0393701, 'Feet': 0.00328084, 'Yards': 0.00109361, 'Centimeters': 0.1, 'Millimeters': 1},
    },
    'Weight': {
        'Milligrams': {'Milligrams': 1, 'Grams': 0.001, 'Kilograms': 0.000001, 'Pounds': 0.00000220462, 'Ounces': 0.000035274},
        'Grams': {'Milligrams': 1000, 'Grams': 1, 'Kilograms': 0.001, 'Pounds': 0.00220462, 'Ounces': 0.035274},
        'Kilograms': {'Milligrams': 1000000, 'Grams': 1000, 'Kilograms': 1, 'Pounds': 2.20462, 'Ounces': 35.274},
        'Pounds': {'Milligrams': 453592, 'Grams': 453.592, 'Kilograms': 0.453592, 'Pounds': 1, 'Ounces': 16},
        'Ounces': {'Milligrams': 28349.5, 'Grams': 28.3495, 'Kilograms': 0.0283495, 'Pounds': 0.0625, 'Ounces': 1},
    },
    'Volume': {
        'Liters': {'Liters': 1, 'Milliliters': 1000, 'Gallons': 0.264172, 'Fluid Ounces': 33.814, 'Cubic Meters': 0.001, 'Cubic Centimeters': 1000, 'Cubic Kilometers': 1e-12, 'Cubic Millimeters': 1e+6},
        'Milliliters': {'Liters': 0.001, 'Milliliters': 1, 'Gallons': 0.000264172, 'Fluid Ounces': 0.033814, 'Cubic Meters': 1e-6, 'Cubic Centimeters': 1, 'Cubic Kilometers': 1e-15, 'Cubic Millimeters': 1000},
        'Gallons': {'Liters': 3.78541, 'Milliliters': 3785.41, 'Gallons': 1, 'Fluid Ounces': 128, 'Cubic Meters': 0.00378541, 'Cubic Centimeters': 3785.41, 'Cubic Kilometers': 3.78541e-12, 'Cubic Millimeters': 3.78541e+6},
        'Fluid Ounces': {'Liters': 0.0295735, 'Milliliters': 29.5735, 'Gallons': 0.0078125, 'Fluid Ounces': 1, 'Cubic Meters': 2.95735e-5, 'Cubic Centimeters': 29.5735, 'Cubic Kilometers': 2.95735e-14, 'Cubic Millimeters': 29573.5},
        'Cubic Meters': {'Liters': 1000, 'Milliliters': 1e+6, 'Gallons': 264.172, 'Fluid Ounces': 33814, 'Cubic Meters': 1, 'Cubic Centimeters': 1e+6, 'Cubic Kilometers': 1e-9, 'Cubic Millimeters': 1e+9},
        'Cubic Centimeters': {'Liters': 0.001, 'Milliliters': 1, 'Gallons': 0.000264172, 'Fluid Ounces': 0.033814, 'Cubic Meters': 1e-6, 'Cubic Centimeters': 1, 'Cubic Kilometers': 1e-15, 'Cubic Millimeters': 1000},
        'Cubic Kilometers': {'Liters': 1e+12, 'Milliliters': 1e+15, 'Gallons': 2.64172e+11, 'Fluid Ounces': 3.3814e+13, 'Cubic Meters': 1e+9, 'Cubic Centimeters': 1e+15, 'Cubic Kilometers': 1, 'Cubic Millimeters': 1e+18},
        'Cubic Millimeters': {'Liters': 1e-6, 'Milliliters': 0.001, 'Gallons': 2.64172e-7, 'Fluid Ounces': 3.3814e-5, 'Cubic Meters': 1e-9, 'Cubic Centimeters': 0.001, 'Cubic Kilometers': 1e-18, 'Cubic Millimeters': 1},
    },
    'Time': {
        'Seconds': {
            'Seconds': 1,
            'Milliseconds': 1000,
            'Microseconds': 1e6,
            'Nanoseconds': 1e9,
            'Picoseconds': 1e12,
            'Minutes': 1 / 60,
            'Hours': 1 / 3600,
            'Days': 1 / 86400,
            'Weeks': 1 / 604800,
            'Months': 1 / 2.628e6,
            'Years': 1 / 3.154e7
        },
        'Milliseconds': {
            'Seconds': 0.001,
            'Milliseconds': 1,
            'Microseconds': 1000,
            'Nanoseconds': 1e6,
            'Picoseconds': 1e9,
            'Minutes': 1 / 60000,
            'Hours': 1 / 3.6e6,
            'Days': 1 / 8.64e7,
            'Weeks': 1 / 6.048e8,
            'Months': 1 / 2.628e9,
            'Years': 1 / 3.154e10
        },
        'Microseconds': {
            'Seconds': 1e-6,
            'Milliseconds': 0.001,
            'Microseconds': 1,
            'Nanoseconds': 1000,
            'Picoseconds': 1e6,
            'Minutes': 1 / 6e7,
            'Hours': 1 / 3.6e9,
            'Days': 1 / 8.64e10,
            'Weeks': 1 / 6.048e11,
            'Months': 1 / 2.628e12,
            'Years': 1 / 3.154e13
        },
        'Nanoseconds': {
            'Seconds': 1e-9,
            'Milliseconds': 1e-6,
            'Microseconds': 0.001,
            'Nanoseconds': 1,
            'Picoseconds': 1000,
            'Minutes': 1 / 6e10,
            'Hours': 1 / 3.6e12,
            'Days': 1 / 8.64e13,
            'Weeks': 1 / 6.048e14,
            'Months': 1 / 2.628e15,
            'Years': 1 / 3.154e16
        },
        'Picoseconds': {
            'Seconds': 1e-12,
            'Milliseconds': 1e-9,
            'Microseconds': 1e-6,
            'Nanoseconds': 0.001,
            'Picoseconds': 1,
            'Minutes': 1 / 6e13,
            'Hours': 1 / 3.6e15,
            'Days': 1 / 8.64e16,
            'Weeks': 1 / 6.048e17,
            'Months': 1 / 2.628e18,
            'Years': 1 / 3.154e19
        },
        'Minutes': {
            'Seconds': 60,
            'Milliseconds': 60000,
            'Microseconds': 6e7,
            'Nanoseconds': 6e10,
            'Picoseconds': 6e13,
            'Minutes': 1,
            'Hours': 1 / 60,
            'Days': 1 / 1440,
            'Weeks': 1 / 10080,
            'Months': 1 / 43800,
            'Years': 1 / 525600
        },
        'Hours': {
            'Seconds': 3600,
            'Milliseconds': 3.6e6,
            'Microseconds': 3.6e9,
            'Nanoseconds': 3.6e12,
            'Picoseconds': 3.6e15,
            'Minutes': 60,
            'Hours': 1,
            'Days': 1 / 24,
            'Weeks': 1 / 168,
            'Months': 1 / 730,
            'Years': 1 / 8760
        },
        'Days': {
            'Seconds': 86400,
            'Milliseconds': 8.64e7,
            'Microseconds': 8.64e10,
            'Nanoseconds': 8.64e13,
            'Picoseconds': 8.64e16,
            'Minutes': 1440,
            'Hours': 24,
            'Days': 1,
            'Weeks': 1 / 7,
            'Months': 1 / 30.44,
            'Years': 1 / 365.25
        },
        'Weeks': {
            'Seconds': 604800,
            'Milliseconds': 6.048e8,
            'Microseconds': 6.048e11,
            'Nanoseconds': 6.048e14,
            'Picoseconds': 6.048e17,
            'Minutes': 10080,
            'Hours': 168,
            'Days': 7,
            'Weeks': 1,
            'Months': 1 / 4.345,
            'Years': 1 / 52.143
        },
        'Months': {
            'Seconds': 2.628e6,
            'Milliseconds': 2.628e9,
            'Microseconds': 2.628e12,
            'Nanoseconds': 2.628e15,
            'Picoseconds': 2.628e18,
            'Minutes': 43800,
            'Hours': 730,
            'Days': 30.44,
            'Weeks': 4.345,
            'Months': 1,
            'Years': 1 / 12
        },
        'Years': {
            'Seconds': 3.154e7,
            'Milliseconds': 3.154e10,
            'Microseconds': 3.154e13,
            'Nanoseconds': 3.154e16,
            'Picoseconds': 3.154e19,
            'Minutes': 525600,
            'Hours': 8760,
            'Days': 365.25,
            'Weeks': 52.143,
            'Months': 12,
            'Years': 1
        }
    },
 'Temperature': {
    'Celsius': {
        'Celsius': 1,
        'Kelvin': lambda c: c + 273.15,
        'Fahrenheit': lambda c: (c * 9/5) + 32
    },
    'Kelvin': {
        'Celsius': lambda k: k - 273.15,
        'Kelvin': 1,
        'Fahrenheit': lambda k: (k - 273.15) * 9/5 + 32
    },
    'Fahrenheit': {
        'Celsius': lambda f: (f - 32) * 5/9,
        'Kelvin': lambda f: (f - 32) * 5/9 + 273.15,
        'Fahrenheit': 1}
    }
}

# Functions to update units and perform conversion
def update_units(*args):
    category = category_var.get()
    units = list(conversion_factors[category].keys())
    from_unit_var.set(units[0])
    to_unit_var.set(units[0])
    from_unit_menu['menu'].delete(0, 'end')
    to_unit_menu['menu'].delete(0, 'end')
    for unit in units:
        from_unit_menu['menu'].add_command(label=unit, command=tk._setit(from_unit_var, unit))
        to_unit_menu['menu'].add_command(label=unit, command=tk._setit(to_unit_var, unit))


def perform_conversion():
    category = category_var.get()
    from_unit = from_unit_var.get()
    to_unit = to_unit_var.get()
    amount = float(amount_entry.get())

    # Retrieve the conversion factor or function
    factor = conversion_factors[category][from_unit][to_unit]

    # Check if the factor is a function (lambda), and use it if so
    if callable(factor):
        result = factor(amount)
    else:
        result = amount * factor

    if result < 0.001 and result > -0.001:
        result_label.config(
            text=f'{amount} {from_unit} = {result:.1e} {to_unit}')  # Scientific notation for very small values
    elif result >= 10000 or result <= -10000:
        result_label.config(
            text=f'{amount} {from_unit} = {result:.1e} {to_unit}')  # Scientific notation for large values
    else:
        result_label.config(text=f'{amount} {from_unit} = {result:.4f} {to_unit}')  # Regular format for normal values
# Initialize the main window

root = tk.Tk()
root.title("Unit Converter App")
root.geometry('600x645')
root.config(bg='#5effbc')
root.resizable(False, False)

style = ttk.Style()
style.configure("TMenubutton", font="Calibri 15 bold",background='#feb002')

logo = tk.PhotoImage(file='logo.png')
tk.Label(root, image=logo, bg='#5effbc') \
    .place(x=230, y=15)
tk.Label(root, text='Unit Converter', font="Calibri 35 bold",
         fg='black', bg='#5effbc').place(x=150, y=162)


# Dropdown for selecting the category
category_var = tk.StringVar(value='Length')
category_label = tk.Label(root, text="Category:",
                          font='Calibri 15 bold',bg='#5effbc')
category_label.place(x=190, y=260)
category_menu = ttk.OptionMenu(root, category_var, 'Length',
                    *conversion_factors.keys(), command=update_units)

# category_menu.config(font=('Helvetica', 12))
category_menu.place(x=280, y=260)

# Dropdowns for selecting units
from_unit_var = tk.StringVar(value='Meters')
to_unit_var = tk.StringVar(value='Meters')

from_unit_label = tk.Label(root, text="From Unit:",
                           font='Calibri 15 bold',bg='#5effbc')
from_unit_label.place(x=60, y=330)
from_unit_menu = ttk.OptionMenu(root, from_unit_var, 'Meters', '')
from_unit_menu.place(x=160, y=330)

to_unit_label = tk.Label(root, text="To Unit:",
                         font='Calibri 15 bold',bg='#5effbc')
to_unit_label.place(x=340, y=330)
to_unit_menu = ttk.OptionMenu(root, to_unit_var, 'Meters', '')
to_unit_menu.place(x=417, y=330)

# Entry field for the amount
amount_label = tk.Label(root, text="Enter Amount:",
                        font='Calibri 15 bold',bg='#5effbc')
amount_label.place(x=60, y=415)
amount_entry = tk.Entry(root,width=15,bd=2,font='Calibri 15 bold')
amount_entry.place(x=192, y=415)

# Button to perform conversion
convert_button = tk.Button(root, text="Convert",
                           command=perform_conversion,
                           font='Calibri 15 bold', fg='#5effbc',
                           bg='#ff0038',height='1',width=9)
convert_button.place(x=370, y=410)

# Label to display the result
result_label = tk.Label(root, text="Result: ",
                        font='Calibri 15 bold',bg='#5effbc')
result_label.place(x=60, y=500)

# Insta page
insta_page=tk.Label(root,text="@pythonagham",bg='#5effbc',
              fg='black',font='arial 10 bold italic')
insta_page.place(x=250,y=600)


# Initialize the units based on the default category
update_units()

# Run the Tkinter main loop
root.mainloop()
