# CCTV Dataset Inventory — Transjakarta BRT

- **Last updated:**
- **Prepared by:**
- **Dataset location (path):**
- **Total records:**

---

## Quick Summary

| Metric | Value |
|---|---|
| Total video files | |
| Total usable files | |
| Total duration (hrs) | |
| Date range | |
| Stations covered | |
| Corridors covered | |

---

## Field Legend

| Field | Description | Values |
|---|---|---|
| **ID** | Sequential record number | 001, 002, ... |
| **Date** | Recording date | DD/MM/YYYY |
| **Day** | Day type | Weekday / Weekend / Holiday |
| **Period** | Time-of-day classification | Peak AM / Peak PM / Off-Peak |
| **Time Start** | Recording start time | HH:MM |
| **Time End** | Recording end time | HH:MM |
| **Duration** | Length of footage | Minutes |
| **Station** | Transjakarta stop/station name | e.g., Harmoni, Dukuh Atas |
| **Corridor** | Transjakarta corridor | e.g., Corridor 1, Corridor 6 |
| **Docking Bay Captured** | The specific docking bay (stopping bay) the platform camera captures clearly — the area within a sub-stop where BRT vehicles pull up to allow customers to board or alight (ITDP); one station may have multiple docking bays | e.g., Bay 1, Bay 2, Bay 1 & 2 |
| **Bay Coverage** | How clearly the docking bay is captured within the camera frame | Full / Partial / Multi-bay |
| **Quality** | Video image quality | Good / Fair / Poor |
| **Visibility** | Camera obstruction status | Clear / Partial / Obstructed |
| **Usable** | Suitability for analysis | Yes / Partial / No |
| **File Name** | Actual file name on disk | e.g., cctv_harmoni_20250601_0730.mp4 |
| **File Size** | File size | e.g., 2.3 GB |
| **Notes** | Any remarks, issues, or observations | Free text |

---

## Inventory

### Cawang Sentral

| ID | Date | Day | Period | Time Start | Time End | Duration (min) | Corridor | Docking Bay Captured | Bay Coverage | Quality | Visibility | Usable | File Name | File Size | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 001 | 25/10/2025 | Weekend | Off-Peak | 10:00 | 11:00 | 60 |  | H, J, K, L | Multi-bay | Fair | Partial | Partial | cs_25_1011_HJKL.avi | 294 MB | Passenger boarding/alighting dynamics slightly obstructed by ceiling fan; docking bays H and L slightly obstructed by signage; docking bays J and K are a bit too far to see clearly; glitch at 10:18 |
| 002 | 25/10/2025 | Weekend | Off-Peak | 10:00 | 11:00 | 60 | Cannot be identified | Cannot be identified | Cannot be identified | Poor | Obstructed | No | cs_25_1011_priuk.avi | 111 MB | Visibility is not fully clear, so the docking bay captured cannot be identified; passenger boarding/alighting dynamics cannot be captured, so this footage cannot be used for further analysis |
| 003 | 25/10/2025 | Weekend | Off-Peak | 10:00 | 10:36 | 36 |  | D, E, P, R | Multi-bay | Fair | Partial | Partial | cs_25_1011_R_1000_1036.avi | 137 MB | Docking bay D fully obstructed by signage; docking bay E partially obstructed by signage; docking bay R partially obstructed by signage and tenant shop near docking R; docking bay P is partially obstructed |
| 004 | 25/10/2025 | Weekend | Off-Peak | 10:36 | 11:00 | 24 |  | D, E, P, R | Multi-bay | Fair | Partial | Partial | cs_25_1011_R_1036_1100.avi | 85 MB | Docking bay D fully obstructed by signage; docking bay E partially obstructed by signage; docking bay R partially obstructed by signage and tenant shop near docking R; docking bay P is partially obstructed |
| 005 | 25/10/2025 | Weekend | Off-Peak | 17:00 | 18:00 | 60 |  | H, J, K, L | Multi-bay | Fair | Partial | Partial | cs_25_1718_HJKL.avi | 300 MB | Passenger boarding/alighting dynamics slightly obstructed by ceiling fan; docking bays H and L slightly obstructed by signage; docking bays J and K are a bit too far to see clearly |
| 006 | 25/10/2025 | Weekend | Off-Peak | 17:00 | 18:00 | 60 | Cannot be identified | Cannot be identified | Cannot be identified | Poor | Obstructed | No | cs_25_1718_priuk.avi | 186 MB | Visibility is not fully clear, so the docking bay captured cannot be identified; passenger boarding/alighting dynamics cannot be captured, so this footage cannot be used for further analysis |
| 007 | 25/10/2025 | Weekend | Off-Peak | 17:00 | 18:00 | 60 |  | D, E, P, R | Multi-bay | Fair | Partial | Partial | cs_25_1718_R.avi | 187 MB | Docking bay D fully obstructed by signage; docking bay E partially obstructed by signage; docking bay R partially obstructed by signage and tenant shop near docking R; docking bay P is partially obstructed |
| 008 | 27/10/2025 | Weekday | Peak AM | 07:00 | 08:00 | 60 |  | H, J, K, L | Multi-bay | Fair | Partial | Partial | cs_27_0708_HJKL.avi | 317 MB | Passenger boarding/alighting dynamics slightly obstructed by ceiling fan; docking bays H and L slightly obstructed by signage; docking bays J and K are a bit too far to see clearly |
| 009 | 27/10/2025 | Weekday | Peak AM | 07:00 | 08:00 | 60 | Cannot be identified | Cannot be identified | Cannot be identified | Poor | Obstructed | No | cs_27_0708_priuk.avi | 147 MB | Visibility is not fully clear, so the docking bay captured cannot be identified; passenger boarding/alighting dynamics cannot be captured, so this footage cannot be used for further analysis |
| 010 | 27/10/2025 | Weekday | Peak AM | 07:00 | 07:53 | 53 |  | D, E, P, R | Multi-bay | Fair | Partial | Partial | cs_27_0708_R_0700_0753.avi | 205 MB | Docking bay D fully obstructed by signage; docking bay E partially obstructed by signage; docking bay R partially obstructed by signage and tenant shop near docking R; docking bay P is partially obstructed |
| 011 | 27/10/2025 | Weekday | Peak AM | 07:53 | 08:00 | 7 |  | D, E, P, R | Multi-bay | Fair | Partial | Partial | cs_27_0708_R_0753_0800.avi | 30 MB | Docking bay D fully obstructed by signage; docking bay E partially obstructed by signage; docking bay R partially obstructed by signage and tenant shop near docking R; docking bay P is partially obstructed |
| 012 | 27/10/2025 | Weekday | Off-Peak | 13:00 | 14:00 | 60 |  | H, J, K, L | Multi-bay | Fair | Partial | Partial | cs_27_1314_HJKL.avi | 291 MB | Passenger boarding/alighting dynamics slightly obstructed by ceiling fan; docking bays H and L slightly obstructed by signage; docking bays J and K are a bit too far to see clearly |
| 013 | 27/10/2025 | Weekday | Off-Peak | 13:00 | 14:00 | 60 | Cannot be identified | Cannot be identified | Cannot be identified | Poor | Obstructed | No | cs_27_1314_priuk.avi | 145 MB | Visibility is not fully clear, so the docking bay captured cannot be identified; passenger boarding/alighting dynamics cannot be captured, so this footage cannot be used for further analysis |
| 014 | 27/10/2025 | Weekday | Off-Peak | 13:00 | 14:00 | 60 |  | D, E, P, R | Multi-bay | Fair | Partial | Partial | cs_27_1314_R.avi | 182 MB | Docking bay D fully obstructed by signage; docking bay E partially obstructed by signage; docking bay R partially obstructed by signage and tenant shop near docking R; docking bay P is partially obstructed |
| 015 | 27/10/2025 | Weekday | Peak PM | 17:30 | 18:30 | 60 |  | H, J, K, L | Multi-bay | Fair | Partial | Partial | cs_27_17301830_HJKL.avi | 222 MB | Passenger boarding/alighting dynamics slightly obstructed by ceiling fan; docking bays H and L slightly obstructed by signage; docking bays J and K are a bit too far to see clearly |
| 016 | 27/10/2025 | Weekday | Peak PM | 17:30 | 18:30 | 60 | Cannot be identified | Cannot be identified | Cannot be identified | Poor | Obstructed | No | cs_27_17301830_priuk.avi | 243 MB | Visibility is not fully clear, so the docking bay captured cannot be identified; passenger boarding/alighting dynamics cannot be captured, so this footage cannot be used for further analysis |
| 017 | 27/10/2025 | Weekday | Peak PM | 17:30 | 18:11 | 41 |  | D, E, P, R | Multi-bay | Fair | Partial | Partial | cs_27_17301830_R_1730_1811.avi | 104 MB | Docking bay D fully obstructed by signage; docking bay E partially obstructed by signage; docking bay R partially obstructed by signage and tenant shop near docking R; docking bay P is partially obstructed |
| 018 | 27/10/2025 | Weekday | Peak PM | 18:11 | 18:30 | 19 |  | D, E, P, R | Multi-bay | Fair | Partial | Partial | cs_27_17301830_1811_1830.avi | 59 MB | Docking bay D fully obstructed by signage; docking bay E partially obstructed by signage; docking bay R partially obstructed by signage and tenant shop near docking R; docking bay P is partially obstructed |
| 019 | | | | | | | | | | | | | | | |
| 020 | | | | | | | | | | | | | | | |

### Galunggung

| ID | Date | Day | Period | Time Start | Time End | Duration (min) | Corridor | Docking Bay Captured | Bay Coverage | Quality | Visibility | Usable | File Name | File Size | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 001 | 25/10/2025 | Weekend | Off-Peak | 10:00 | 11:00 | 60 |  | A,B,C,K,L,M | Multi-bay | Good | Partial | Partial | g_25_1011_BCKL.avi | 215 MB | Docking bays A and M fully clear; docking bays B and L partially obstructed by signage; docking bays C and K fully obstructed by signage |
| 002 | 25/10/2025 | Weekend | Off-Peak | 10:00 | 11:00 | 60 | Cannot be identified | Cannot be identified | Cannot be identified | Good | Clear | Yes | g_25_1011_between.avi | 173 MB | This camera is located on passage connecting alighting-only platform and boarding-only platform |
| 003 | 25/10/2025 | Weekend | Off-Peak | 10:00 | 10:38 | 38 |  | D,E,F,G,H,J | Multi-bay | Good | Partial | Partial | g_25_1011_EFGH_1000_1038.avi | 175 MB | Passenger boarding/alighting dynamics on docking bays D, E, H, and J fully clear; docking bays F and G fully obstructed |
| 004 | 25/10/2025 | Weekend | Off-Peak | 10:38 | 11:00 | 22 |  | D,E,F,G,H,J | Multi-bay | Good | Partial | Partial | g_25_1011_EFGH_1038_1100.avi | 94 MB | Passenger boarding/alighting dynamics on docking bays D, E, H, and J fully clear; docking bays F and G fully obstructed |
| 005 | 25/10/2025 | Weekend | Off-Peak | 10:00 | 11:00 | 60 |  | K,L,M,A,B,C | Multi-bay | Good | Partial | Partial | g_25_1011_KLBC.avi | 191 MB | Docking bays K, L, B, and C fully clear; docking bays M and A partially obstructed by ceiling fan and signage |
| 006 | 25/10/2025 | Weekend | Off-Peak | 17:00 | 18:00 | 60 |  | G,H,E,F | Multi-bay | Good | Partial | Partial | g_25_1718_GHEF.avi | 291 MB | Docking bays G and F are clear; docking bays H and E partially obstructed by signage |
| 007 | | | | | | | | | | | | | | | |
| 008 | | | | | | | | | | | | | | | |

### Petamburan

| ID | Date | Day | Period | Time Start | Time End | Duration (min) | Corridor | Docking Bay Captured | Bay Coverage | Quality | Visibility | Usable | File Name | File Size | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 001 | 25/10/2025 | Weekend | Off-Peak | 10:00 | 11:00 | 60 |  | A,B | Multi-bay | Fair | Partial | Partial | p_25_1011_AB.avi | 176 MB | Docking bays A and B are clear |
| 002 | 25/10/2025 | Weekend | Off-Peak | 10:00 | 11:00 | 60 |  | C,B| Multi-bay| Fair| Partial| Partial| p_25_1011_CBA.avi| 372 MB| Docking bay C is partially obstructed by signage, docking bay B is partially obstructed by ceiling fan|
| 003 | 25/10/2025| Weekend| Off-Peak| 10:00| 10:12| 12| | D,E,F| Multi-bay| Fair| Partial| Partial| p_25_1011_EF_1000_1012.avi| 32 MB| Docking D is fully clear, docking E is partially obstructed by ceiling fan, docking F is partially clear since too far|
| 004 | 25/10/2025| Weekend| Off-Peak| 10:12| 11:00| 48| | D,E,F| Multi-bay| Fair| Partial| Partial| p_25_1011_EF_1012_1100.avi| 126 MB| Docking D is fully clear, docking E is partially obstructed by ceiling fan, docking F is partially clear since too far|
| 005 | 25/10/2025 | Weekend | Off-Peak | 10:00 | 11:00 | 60 | | F,E,D| Multi-bay| Poor| Partial| Partial| p_25_1011_F.avi| 239 MB| The quality of video is blur, some part appears red and blue color, but visibility of docking bays are partially clear (F and E), docking bay D too far|
| 006 | 25/10/2025 | Weekend | Off-Peak | 10:00 | 11:00 | 60 | | G,H| Multi-bay| Poor| Partial| Partial| p_25_1011_GH.avi| 188 MB| Video is blur, docking bay G is partially cropped out (outframe), docking H is partially obstructed by ceiling fan and signage|
| 007 | 25/10/2025| Weekend| Off-Peak| 10:00| 10:51| 51| | J,H| Multi-bay| Poor| Partial| Partial| p_25_1011_H_1000_1051.avi| 341 MB| The video exhibits severe frame ghosting and temporal blending, causing subjects to appear semi-transparent and duplicated across the frame|
| 008 | 25/10/2025| Weekend| Off-Peak| 10:51| 11:00| 9| | J,H| Multi-bay| Poor| Partial| Partial| p_25_1011_H_1051_1100.avi| 56 MB| The video exhibits severe frame ghosting and temporal blending, causing subjects to appear semi-transparent and duplicated across the frame|
| 009 | 25/10/2025| Weekend| Off-Peak| 10:00| 10:01| 1| | K,L,M| Multi-bay| Good| Partial| Yes| p_25_1011_LM_1001.avi| 2 MB| Docking bays K,L,M are clear |
| 010 | 25/10/2025| Weekend| Off-Peak| 10:01| 11:00| 59| | K,L,M| Multi-bay| Good| Partial| Yes| p_25_1011_LM_1001.avi| 347 MB| Docking bays K,L,M are clear |
| 011 | 25/10/2025| Weekend| Off-Peak| 10:00| 11:00| 60| | M,L,K| Multi-pay| Good| Partial| Yes| p_25_1011_ML.avi| 327 MB| Docking bays M,L,K are clear, but docking bay K too bit far|

---

## Notes

