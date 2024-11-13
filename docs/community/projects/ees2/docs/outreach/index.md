---
title: ""
---
[Back to EES2 Project page](https://linked.art/community/projects/ees2/)

# EES2 trial of Quire and Linked Art with Cheney School

## Incorporating new technologies within museum education and outreach activities

In October 2024 the Enriching Exhibition Stories (EES2) team ran a trial alongside staff and students from [Cheney School](https://www.cheneyschool.org/) in Oxford. Our collective aim was to develop a programme of materials and activities to support students’ creation of digital stories drawn from their reflections about museum objects both in the Ashmolean Museum’s collections and those of the school’s own Rumble Museum.

Following several months of collaboration and preparation, a programme was organised consisting of three interlinked activities.

The first activity was a **visit to the Ashmolean Museum** in Oxford. Students studying history or computing were offered the opportunity to attend, from which 24 students from Cheney School were selected, most of whom had never visited the museum. This intersection of subjects was chosen by the school to mix students whose choice of computing might usually distance them from engaging with historical sources; and vice versa. During the visit the class was split in two, with each half alternating between an object handling session led by a museum curator; and a gallery hunt led by a member of the audiences and engagement team. In both of these activities students completed structured worksheets to collect observations about the objects they saw; and were prompted to reflect upon and record their own interpretations. These observations and interpretations were kept to be used as part of subsequent activities.

The second activity was a **Rumble Museum Workshop** at Cheney School, led by a history teacher and the director of the Rumble Museum. Students worked in the same pairs as during their Ashmolean visit, and were asked to write up their interpretations from that visit in a word processor (GoogleDoc), using formatting, in preparation for the final History and Computing workshop. Students were then asked to take part in a parallel handling session of objects from the Rumble Museum, completing the same structured documentation as at the Ashmolean. Objects were selected for thematic association with those studied at the Ashmolean to encourage consideration of equivalences between the two museums and their collection, and similarly between the responsibilities and opportunities found in running both museums.

The culmination of the programme was a **History and Computing Workshop** led by two computer science teachers. The workshop aimed to demonstrate a variety of information
organisation tools and techniques as the foundation for students’ critical evaluation when encoding and sharing (cultural) information. Working in their pairs, the students were asked to contribute to a collective Quire book documenting their observations and interpretations of museum objects, which the school could publish. They achieved this by (i) supplementing Quire object YAML imported from Linked Art with observations from their handling sessions, learning about the relative strengths of JSON-LD and YAML, the information impacts of conversion between them, and situating YAML in curriculum contexts such as key-value pairs and Python dictionaries; (ii) marking-up their interpretations about objects as a Markdown page for the book, situating Markdown in the curriculum context of HTML, using identifiers to add their YAML object data to their Markdown story, and hyperlinking their own object photos into their stories.

To realise the workshop during the limited preparation time available for the trial, the research team set up a bespoke laptop with an installation of Quire and the [EES2 Linked Art Extension](https://linked.art/community/projects/ees2/docs/quire/), alongside a pre-prepared Quire template, which was used extensively during the workshop. Outside of this initial trial, it is assumed and agreed that a school would install their own copy of this software on an appropriate machine. While Quire need only run on one machine during the lesson, which can be displayed to the whole class, a mechanism for student pairs to transfer their YAML and Markdown onto that machine is required for the class book to be compiled. For the trial a shared Google Drive was used, this being the chosen platform for Cheney School, with a Google Drive Sync app used to make a mirrored copy on the Quire laptop (a cloud-based/non-mirrored copy of the files was found to be insufficiently performant). Permissions were set to allow students to edit their content, but not the entire Quire project; the book was compiled by the teacher in plenary; students could then view Quire outputs (e.g. the PDF of the book) during the workshop.

## Resources
Further details about the approach of the trial are documented in the resources below. These were created collaboratively between the research team and school staff, with specific [contributions noted in square brackets]. A full list of acknowledgements can be found below.

**Ashmolean Museum Visit**: Run as a 1 hour Handling Session, 1 hour Gallery Hunt, plus unguided time to explore. An additional hour is recommended*

- Handling Session Activity Plan ([PDF](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/ashmolean_visit/ashmolean_handling-activity_plan.pdf)|[docx](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/ashmolean_visit/ashmolean_gallery-activity_plan.docx)) [Andrew Shapland]
- Handling Session Worksheet ([PDF](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/ashmolean_visit/ashmolean_handling-worksheet.pdf)|[docx](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/ashmolean_visit/ashmolean_handling-worksheet.docx)) [Andrew Shapland]
- Gallery Session Activity Plan ([PDF](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/ashmolean_visit/ashmolean_gallery-activity_plan.pdf)|[docx](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/ashmolean_visit/ashmolean_gallery-activity_plan.docx)) [Kirsti Deacon]
- Gallery Hunt Worksheet ([PDF](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/ashmolean_visit/ashmolean_gallery-worksheet.pdf)|[docx](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/ashmolean_visit/ashmolean_gallery-worksheet.docx)) [Kirsti Deacon]

**Rumble Museum Workshop**: Run as a 1 hour lesson. 2 hours are recommended*

- Lesson Plan ([PDF](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/rumble_workshop/rumble_workshop-lesson_plan.pdf)|[docx](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/rumble_workshop/rumble_workshop-lesson_plan.docx)) [Louise Elias, Lorna Robinson, and Martin Daniels]
- Lesson Slides ([PDF](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/rumble_workshop/rumble_workshop-lesson_slides.pdf)|[pptx](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/rumble_workshop/rumble_workshop-lesson_slides.pptx)) [Lorna Robinson]
- Handling Worksheet ([PDF](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/rumble_workshop/rumble_workshop-handling_worksheet.pdf)|[docx](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/rumble_workshop/rumble_workshop-handling_worksheet.docx)) [Andrew Shapland]

**History & Computing Workshop**: Two 1 hour lessons either side of a lunch break, 3 hours are recommended*

- Pre-workshop setup and configuration checklist ([PDF](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/history_computing_workshop/history_and_computing_workshop-checklist.pdf)|[docx](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/history_computing_workshop/history_and_computing_workshop-checklist.docx)) [Kevin Page]  
    - Creating a new template for different museum objects would require installation of Quire and the Linked Art Extension [Tyler Bonnet] created for the EES2 project  
- Lesson Plan ([PDF](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/history_computing_workshop/history_and_computing_workshop-lesson_plan.pdf)|[docx](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/history_computing_workshop/history_and_computing_workshop-lesson_plan.docx)) [Louise Elias and Kevin Page]  
    - N.B. Actual timing during the trial did not keep to the lesson plan: most students completed the tasks noted in the lesson plan at 60 minutes in the first lesson (i.e. up to the lunch break); some also completed tasks noted in the lesson plan up to 20 minutes in the second lesson (after lunch break); later tasks were not completed in the trial due to lack of time*  
- Lesson Slides ([PDF](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/history_computing_workshop/history_and_computing_workshop-lesson_slides.pdf)|[pptx](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/history_computing_workshop/history_and_computing_workshop-lesson_slides.pptx)) [Louise Elias, Kevin Page, and Tyler Bonnet]  
- Video demonstrating Linked Art data import to Quire ([mp4](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/history_computing_workshop/quire_linked_art_demo_video.mp4)|[YouTube](https://youtu.be/PAYuN2hj2nE))  
- Student Worksheet ([PDF](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/history_computing_workshop/history_and_computing_workshop-student_worksheet.pdf)|[docx](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/history_computing_workshop/history_and_computing_workshop-student_worksheet.docx)) [Tyler Bonnet, Kevin Page, and Clare Llewellyn]  
- Markdown Reference Sheet for students ([PDF](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/history_computing_workshop/history_and_computing_workshop-student_markdown_reference_sheet.pdf)|[docx](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/history_computing_workshop/history_and_computing_workshop-student_markdown_reference_sheet.docx)) [Tyler Bonnet]  
- ‘cheney_book’ Quire project folder ([Zip](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/history_computing_workshop/cheney_book.zip)) [Tyler Bonnet and Kevin Page]  
    - This is the “blank” project folder pre-populated with templates ready for observations and interpretations to be added by students during the class (by following the lesson plan and worksheet)  
- Linked Art data export ([Zip](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/history_computing_workshop/linked_art_export.zip)) [Tyler Bonnet]  
    - A copy of Ashmolean and Rumble Museum Linked Art data, specially provided for this classroom exercise, used in creation of the cheney_book template, and provided here for reference. Ashmolean data and images are © Ashmolean Museum, University of Oxford  
- IIIF data export ([Zip](https://github.com/oerc-csi/la-quire/raw/main/docs/history_and_computing_lesson/history_computing_workshop/iiif_export.zip)) [Tyler Bonnet]  
    - A copy of Ashmolean and Rumble Museum IIIF data, specially provided for this classroom exercise, used in creation of the cheney_book template, and provided here for reference. Ashmolean data and images are © Ashmolean Museum, University of Oxford  

\* Based on the novel experience of the trial, all research and school staff agreed that many, if not all, activities in the programme would benefit from additional time allowances, and that completing the full programme would be of benefit to learners: the Ashmolean visit would benefit from additional time to consolidate and complete worksheets; the Rumble Workshop would benefit from being 2 hours in length, and the History & Computing Workshop would benefit from taking place over three 1 hour lessons. Further details can be found in the  Evaluation and Recommendations report created by school staff and the research team, published by Cheney School, and reproduced here by kind permission of Cheney School.

## Acknowledgements and thanks

**Cheney School**  
Rob Pavey (Headteacher)  
Nazneen Ali  
Tapera Chikunga  
Martin Daniels  
Louise Elias  
Sophie Quantrell  
Lorna Robinson  
Cheney IT Support Team  

**Ashmolean Museum University of Oxford**  
Andrew Shapland  
Kirsti Deacon  
Aruna Bhaugeerutty  

**University of Edinburgh**  
Clare Llewellyn  

**University of Oxford e-Research Centre**  
Tyler Bonnet  
Erin Canning  
Thorsteinn Imi King  
Kevin Page  
Sasha Tan  

