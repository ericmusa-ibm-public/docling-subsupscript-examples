# Missed or misrepresented superscripts and subscripts


## High level conclusions
Superscripts and subscripts, especially when in normal text, are sometimes identified correctly with Docling Convert, maybe 50% of the time. However, superscripts and subscripts within tables, e.g., in column or row headers, are rarely identified accurately.

## Documents with missing subscripts and superscripts:

### [report table 1.pdf](example_pdfs/report%20table%201.pdf)
A table from [the 2023 Michigan Potato Research Report](https://www.canr.msu.edu/publications/2023-michigan-potato-research-report?language_id=) that has many superscripts and complex formatting, a lot of which is misinterpreted by the Docling PDF pipeline.

#### Missing:
- Alltogether very rough parsing
- Multi-level headers messed up
- Nearly all superscripts in table missed - handful in headers correct
- Majority of superscripts in the bottom legend *accurately* parsed
---

### [report table 2.pdf](example_pdfs/report%20table%202.pdf)
Another (slightly different) table from [the 2023 Michigan Potato Research Report](https://www.canr.msu.edu/publications/2023-michigan-potato-research-report?language_id=) that has many superscripts and complex formatting, a lot of which is similarly misinterpreted by the Docling PDF pipeline.

#### Overview:
- Alltogether very rough parsing, same as [report table 1.pdf](example_pdfs/report%20table%201.pdf)
- Multi-level headers messed up
- Nearly all superscripts in table missed - handful in headers correct
- Majority of superscripts in the bottom legend *accurately* parsed
---

### [research paper text.pdf](example_pdfs/research%20paper%20text.pdf)
[The first page of] A research publication (of my own writing...) that I know has a few missed superscripts (on the first page).

#### Overview:
- Nearly all superscripts identified correctly. Handful missing from the top line listing authors.
- Even correctly identified the * circle glyphs in the paper, e.g., "14$^{GLYPH<C15>GLYPH<C15>}"
---

### [subscript superscript text.pdf](example_pdfs/subscript%20superscript%20text.pdf)
A test document with numerous superscripts and subscripts written in Word and then exported as a PDF.

#### Overview:
- Mostly good, handfull missed:
- Nulla vehicula$_{15}$ elit$^{!!unum!!}$ non
  - missed superscripting "umum"
- Phasellus et ligula$_{7}$ lorem$^{!!8!!}$ volutpat.
  - missed superscripting "8"
---

### [table 1 superheader.png](example_pdfs/table%201%20superheader.png)
A screenshot of a portion of [report table 1.pdf](example_pdfs/report%20table%201.pdf) that includes both the column and super headers. It has one superscript in the headers and many in the row indices, none of which are interpreted correctly by Docling.

#### Overview:
- Missed the superscript in the main header and placed it inline before the header text.
- Did misinterpreted a number of numerals in the table as well (see [this comparison](output/table%201%20superheader%20comparison.png))
---

### [table 1.png](example_pdfs/table%201.png)
A screenshot of a portion of [report table 1.pdf](example_pdfs/report%20table%201.pdf) that includes just the column headers. It has two superscripts in the column headers and many in the row indices, none of which are interpreted correctly by Docling.

#### Overview:
- Did not identify any of the superscriptsn in the table; there were many superscripts on the row headers.
- Also did not identify a handful of numerals from the table cells.
---

### [table 2 legend.png](example_pdfs/table%202%20legend.png)
A screenshot of a portion of [report table 2.pdf](example_pdfs/report%20table%202.pdf) that includes just the legend items explaining the superscripts in the table above. It has weird formatting that Docling has incorrectly parsed, and has superscripts which are all of the following:
- correctly parsed and interpreted as superscripts
- demoted to inline text, usually preceding the text it is superscripted over
- completely misinterpreted as the wrong character *and* demoted to inline text.

#### Overview:
- Interestingly, did not identify any of the superscripts
- *And* the overall parsing accuracy was significantly worse for the screenshot than the original PDF.
---