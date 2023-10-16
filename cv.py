# -----------------------------------------------------------------------------
# Title: Distinguished Security Engineer CV
# Author: Ikwuka Okoye (@gadcode)
# Date: October 15, 2023
# Usage: This program uses the Python programming language's docx module to 
#        create a professional curriculum vitae (CV).
# -----------------------------------------------------------------------------

from docx import Document


def create_cv():
    # Creates a new Word document
    doc = Document()
    
    # Adds name and contact information
    doc.add_heading('SHALOM GAD', level=1)
    doc.add_paragraph(f'📦 GitHub: [https://github.com/gadcode]')
    doc.add_paragraph(f'📧 E-mail: [shalomgad@proton.me]')
    doc.add_paragraph(f'📜 Certificates: [https://drive.proton.me/urls/96MD0BJ03R#wu0zvy0FCTmx]')
    doc.add_paragraph('📍 Address: 7 Ozara Main Street, 402103, Enugu, Nigeria')
    
    # Adds introduction
    doc.add_heading('DISTINGUISHED SECURITY ENGINEER', level=2)
    doc.add_paragraph(
        "Cybersecurity | Threat Mitigation | Security Solutions | Incident Response | Malware Prevention | Computer Forensics\n"
        "A highly motivated and forward-thinking cybersecurity professional with a strong foundation in software development "
        "and a passion for securing digital environments. Eager to leverage technical expertise, strategic thinking, and "
        "and hands-on experience to protect organizations from cyber threats and ensure a robust security posture."
    )
    
    #Adds key skills
    doc.add_heading('Key Skills', level=2)
    skills = [
        "Cybersecurity Fundamentals",
        "Threat Detection and Mitigation",
        "Security Solutions Design",
        "Incident Response & Forensics",
        "Network & Cloud Security",
        "Vulnerability Assessment",
        "Security Awareness & Training"
    ]
    for skill in skills:
        doc.add_paragraph(f"- {skill}")
