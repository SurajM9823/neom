from fpdf import FPDF

# Create PDF object
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Title
pdf.set_font("Arial", style="B", size=14)
pdf.cell(0, 10, "Answer Key: Class V Computer Science", ln=True, align="C")
pdf.ln(10)

# Section A: Choose the Correct Answer
pdf.set_font("Arial", style="B", size=12)
pdf.cell(0, 10, "Section A: Choose the Correct Answer", ln=True)
pdf.set_font("Arial", size=12)
answers_a = [
    "1. i. Speed",
    "2. i. Mouse",
    "3. iii. Hard disk",
    "4. iii. Both hardware and software",
    "5. iii. Supercomputers",
    "6. ii. Machine language",
    "7. ii. Mouse",
    "8. ii. Laptop",
    "9. i. Ctrl+Z",
    "10. i. Ctrl+S",
]
for ans in answers_a:
    pdf.cell(0, 10, ans, ln=True)

# Section B: Fill in the Blanks
pdf.ln(5)
pdf.set_font("Arial", style="B", size=12)
pdf.cell(0, 10, "Section B: Fill in the Blanks", ln=True)
pdf.set_font("Arial", size=12)
answers_b = [
    "1. computare",
    "2. CPU",
    "3. Hard disk",
    "4. RAM",
    "5. Microphone",
]
for ans in answers_b:
    pdf.cell(0, 10, ans, ln=True)

# Section C: Write the Full Form
pdf.ln(5)
pdf.set_font("Arial", style="B", size=12)
pdf.cell(0, 10, "Section C: Write the Full Form", ln=True)
pdf.set_font("Arial", size=12)
answers_c = [
    "1. ROM: Read-Only Memory",
    "2. RAM: Random Access Memory",
    "3. ALU: Arithmetic Logic Unit",
    "4. GUI: Graphical User Interface",
    "5. CD-ROM: Compact Disc Read-Only Memory",
]
for ans in answers_c:
    pdf.cell(0, 10, ans, ln=True)

# Section D: Write the Steps
pdf.ln(5)
pdf.set_font("Arial", style="B", size=12)
pdf.cell(0, 10, "Section D: Write the Steps", ln=True)
pdf.set_font("Arial", size=12)
answers_d = [
    "1. Steps to set background image:",
    "   a. Right-click on the desktop.",
    "   b. Select 'Personalize' or 'Properties'.",
    "   c. Choose the 'Background' or 'Wallpaper' option.",
    "   d. Select an image and click 'Apply'.",
    "2. Steps to set date and time:",
    "   a. Click on the clock in the taskbar.",
    "   b. Select 'Adjust date and time'.",
    "   c. Change the date and time as required.",
    "   d. Click 'OK' or 'Apply'.",
]
for ans in answers_d:
    pdf.cell(0, 10, ans, ln=True)

# Section E: True or False
pdf.ln(5)
pdf.set_font("Arial", style="B", size=12)
pdf.cell(0, 10, "Section E: True or False", ln=True)
pdf.set_font("Arial", size=12)
answers_e = [
    "1. False",
    "2. True",
    "3. False",
    "4. False",
    "5. True",
]
for ans in answers_e:
    pdf.cell(0, 10, ans, ln=True)

# Section F: Very Short Answer Questions
pdf.ln(5)
pdf.set_font("Arial", style="B", size=12)
pdf.cell(0, 10, "Section F: Very Short Answer Questions", ln=True)
pdf.set_font("Arial", size=12)
answers_f = [
    "1. A computer is an electronic device that processes data to produce information.",
    "2. Two functions of an operating system are managing hardware resources and providing a user interface.",
    "3. RAM is temporary memory, while ROM is permanent memory.",
    "4. The CPU processes instructions and manages data flow in a computer.",
    "5. Input device: Mouse, Output device: Monitor",
    "6. UPS stands for Uninterruptible Power Supply, and its purpose is to provide backup power.",
    "7. Data refers to raw facts and figures.",
    "8. A pen drive is used to store and transfer data.",
    "9. A mouse is used to point, click, and interact with items on the screen.",
    "10. Computers are used in offices and schools for tasks like document preparation, data analysis, and learning.",
]
for ans in answers_f:
    pdf.cell(0, 10, ans, ln=True)

# Save PDF
output_path = "/mnt/data/Class_V_Computer_Science_Answers.pdf"
pdf.output(output_path)

output_path
