"""--------------------------------------------------------------------

Software Design Specification: Comprehensive LaTeX D&D 5e Character
Sheet Generator

-----------------------------------------------------------------------
Project Purpose
-----------------------------------------------------------------------

The goal is to create a GitHub-hosted tool that generates high-quality
LaTeX-based Dungeons & Dragons 5e character sheets. Users will fill out
a form (via a Streamlit front-end) and receive a themed PDF of their
character. This project addresses two core needs:

1. Overcoming D&D Beyond's limitation of six characters per user.

2. Producing customizable and thematic character sheets that enhance
   immersion and flexibility for both players and Dungeon Masters.

-----------------------------------------------------------------------
Scope
-----------------------------------------------------------------------

The tool must generate two distinct character sheet formats:

1. Long (Dungeon Master Introduction Version)
   - Multi-page (3–4 pages).
   - Includes all character information: mechanical, narrative,
     background, equipment, lore, allies, organizations, and other
     flavor details.
   - May feature thematic design elements (e.g., parchment texture,
     colored section headers, decorative fonts).
   - Serves as a comprehensive record at the start of a campaign.

2. Short (Player Gameplay Version)
   - Single-page layout.
   - Contains only the mechanically necessary details (stats, actions,
     spells, HP, equipment critical to play).
   - Designed for rapid reference during gameplay.
   - Black-and-white, minimalistic, and suitable for frequent
     reprinting and pencil annotations.

-----------------------------------------------------------------------
Functional Requirements
-----------------------------------------------------------------------

The generator must:
- Accept structured character input via a form (Streamlit app).
- Compile inputs into two LaTeX templates (long and short versions).
- Output compiled PDFs for download.
- Support customization for aesthetics (e.g., fonts, colors,
  backgrounds).

The character sheet structure includes the following:

1. Basics
   - Character name
   - Class(es) and Level(s)
   - Species
   - Background
   - Experience points

2. Core Stats
   - STR, CON, DEX, INT, WIS, CHA (score + modifier)

3. Other Stats
   - Initiative
   - Armor Class
   - Defenses
   - Proficiency Bonus
   - Speed(s)
   - Hit Points (current/max)
   - Hit Dice

4. Death Saves
   - Success and failure checkboxes

5. Proficiencies and Training
   - Armor
   - Weapons
   - Tools
   - Languages (with source attribution)

6. Actions
   - Standard Actions
   - Bonus Actions
   - Weapon Attacks
   - Cantrips

7. Senses
   - List and sources

8. Class Features
   - Abilities, traits, and features
   - Source attribution (class, species, background, or other)

9. Equipment
   - Items and their sources

10. Spells
   - Known spells
   - Prepared status
   - Mechanical acquisition rules
   - Effects and notes
   - Costs (if applicable)

11. Roleplaying
   - Personality Traits
   - Ideals
   - Bonds
   - Flaws

12. Allies/Organizations
   - Alliances and memberships
   - Explanations of relationships

13. Additional Notes
   - Free-form details not covered elsewhere

-----------------------------------------------------------------------
Design Considerations
-----------------------------------------------------------------------

- A consistent visual identity is desired (e.g., D&D red headers,
  parchment overlay for the long version).
- Layout must balance readability with thematic immersion.
- Templates should be easily extendable for optional rules and homebrew
  content.
- Output should be compatible with both digital (PDF viewing) and
  physical (printing) use.

-----------------------------------------------------------------------
Deliverables
-----------------------------------------------------------------------

1. A LaTeX template for the long version (DM introduction sheet).
   - Multi-page format with rich thematic design.

2. A LaTeX template for the short version (player gameplay sheet).
   - Single-page, black-and-white, practical design.

3. Streamlit application front-end.
   - Interactive form for inputting character details.
   - Two export options: long version PDF, short version PDF.

4. Documentation.
   - Usage instructions for users on GitHub.
   - Guide for extending or modifying templates.

-----------------------------------------------------------------------
Out of Scope
-----------------------------------------------------------------------

- Automatic rules validation (the tool does not enforce D&D 5e rules).
- Third-party data integration (e.g., automated imports from D&D
  Beyond).
- Advanced graphical editing beyond LaTeX’s design capabilities.

-----------------------------------------------------------------------
Next Steps
-----------------------------------------------------------------------

1. Formalize the LaTeX structure for both the long and short templates.
2. Identify reusable macros and environments for consistency across
   templates.
3. Define the Streamlit form fields to match the outlined character
   sheet sections.
4. Prototype PDF generation pipeline.
5. Iterate on aesthetics and usability with sample characters.

--------------------------------------------------------------------"""
