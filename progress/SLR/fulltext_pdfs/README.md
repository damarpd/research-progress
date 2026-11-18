# Full-text articles

Downloaded PDFs for full-text screening. The PDFs are not tracked by git (copyright and size); only this note is.

- Source list: `../fulltext_sheet.xlsx` (178 records, 176 distinct studies). Open an article through the `doi` column; if there is no DOI, search the title in Scopus, Web of Science or Google Scholar.
- File name: `<ft_id>_<screen_id>.pdf`, for example `F001_S094.pdf`. The ids come from the first two columns of the sheet, so a file always maps to one row.
- Download order: the pilot batch first (F001-F020), then the rest in sheet order.
- Record the result in the sheet: `full_text_found` = yes or no. If no, note where you looked in `ft_notes` and use reason 1 ("full text not available") only after trying the DOI, the publisher, Google Scholar, the library and an author copy.
- Companion reports: S407 (companion of S354) and S423 (companion of S051) are read only if needed to see what the conference version adds; the journal version is the main study.
- Keep the PDFs out of the repo; back them up elsewhere if needed.
