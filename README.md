[README (4).md](https://github.com/user-attachments/files/35382868/README.4.md)
# Beyond daily prediction: placing bathing water quality in atmospheric context

The study first describes the weather patterns and rainfall seen during the bathing season and examines their association with observed bathing-water samples. Steps 1–6 then use historical weather and simulated weather sequences to ask how often high-probability days occur and whether they cluster together.

<a id="supporting-analyses"></a>

## Before Step 1 · Weather, rainfall and observed bathing-water samples

**Start with A if you downloaded the study ZIPs.** Follow A–D in order to work through the observed analyses, then continue to [Step 1](#main-analysis). Each of A–D includes its required inputs. You can also rerun any one of them on its own.

| Order | Which ZIP to download | What you will calculate |
| --- | --- | --- |
| A | [weather_pattern_prevalence_publication (1).zip](./weather_pattern_prevalence_publication%20%281%29.zip) | How often each of the 30 weather patterns occurred by month, using daily classifications. |
| B | [SWEW_rainfall_families_publication_v1_0.zip](./SWEW_rainfall_families_publication_v1_0.zip) | The rainfall summaries for each pattern and the checks on their grouping into four families. This uses the supplied rainfall workbook. |
| C | [SWEW_exceedance_associations (1).zip](./SWEW_exceedance_associations%20%281%29.zip) | How bathing-water exceedances differed by weather family on the sampling day. The ZIP includes B’s family assignments and produces the site-day table used by D and Step 5. |
| D | [Antecedent associations.zip](./Antecedent%20associations.zip) | How circulation and rainfall in the three days before sampling were associated with exceedances. The ZIP includes C’s site-day table, Step 4’s historical weather calendar and Step 5’s historical modelling table. |

**If you want to rebuild the rainfall histograms from original radar data**, start with [CEDA processing file and data.zip](./CEDA%20processing%20file%20and%20data.zip) and [CEDA data QA notes.zip](./CEDA%20data%20QA%20notes.zip). The second ZIP contains two documents to read. For the published results, B uses the supplied workbook, which covers 29 dates without a readable histogram in the available archives.

**How to run a package on Windows.** Install Python 3.12. Download the ZIP, right-click it in File Explorer and choose **Extract All**. Open the folder named under the analysis below. Click the File Explorer address bar, type `powershell` and press **Enter**. Run the commands in that window, one line at a time. Open a new PowerShell window in the correct folder for each package.

<details>
<summary><strong>Optional · Raw radar processing and quality checks</strong></summary>

Open the extracted folder containing `All reg log2 and linear 2016 1.py`. To process original NIMROD radar archives, set `base_dir` in a working copy of the script to the folder containing your daily TAR files. Then run:

```powershell
py -3.12 -m pip install numpy pyproj
py -3.12 "All reg log2 and linear 2016 1.py"
```

The script writes daily regional rainfall histograms as CSVs in the working folder. The ZIP includes processed summer histograms. Supply the original daily TAR files separately to repeat the raw processing. [CEDA data QA notes.zip](./CEDA%20data%20QA%20notes.zip) contains two Word documents describing the quality checks. Extract it and open the documents.

</details>

<details open>
<summary><strong>A · weather_pattern_prevalence_publication (1).zip</strong> — calculate monthly weather-pattern frequencies</summary>

Open the folder containing `prevalence_publication.py` and the classification CSV. Run:

```powershell
py -3.12 -m pip install numpy pandas matplotlib
py -3.12 prevalence_publication.py --input "classifications_30regimes(21) (4).csv" --output prevalence_outputs
```

Find the monthly counts, percentages and uncertainty estimates in `prevalence_outputs`.

</details>

<details>
<summary><strong>B · SWEW_rainfall_families_publication_v1_0.zip</strong> — audit the four rainfall families</summary>

Work in a **fresh extraction** of `SWEW_rainfall_families`. The table exporter and verifier read `results/family_mapping`. The commands below regenerate the audit **in that folder**, including its Excel workbook, before exporting and checking the new tables. They replace audit files in your working copy. The plotting command separately reads the stored percentile sheet from the input workbook.

```powershell
py -3.12 -m pip install -r requirements.txt
py -3.12 code/01_weather_pattern_family_mapping.py --output results/family_mapping
py -3.12 code/02_plot_saved_rainfall_summaries.py
py -3.12 code/04_export_publication_tables.py
py -3.12 code/03_verify_results.py --package . --output results/verification/verification_report.json
```

For the commands above, the new mapping is in `results/family_mapping`. Open `storyline_assignments.csv` in that folder and use the `group_final4` column for the manuscript families. The same-day package already includes this table as `data/derived/weather_pattern_family_assignments.csv`.

</details>

<details>
<summary><strong>C · SWEW_exceedance_associations (1).zip</strong> — estimate same-day associations</summary>

Open `SWEW_bathing_water_associations`. Create a local Python environment here because the two observational packages use different versions of statsmodels. The same-day package pins statsmodels 0.14.5 and patsy 1.0.2. The antecedent package pins statsmodels 0.14.6. Use the local environment for each set of commands.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe code/bathing_water_exceedance_associations.py
.\.venv\Scripts\python.exe code/verify_results.py
```

Find the estimates in `results/models` and the tables in `results/tables`. The additional output `results/analysis_data/site_day_analysis.csv` is the frozen site-day reference bundled with Step 5 and the antecedent analysis.

</details>

<details>
<summary><strong>D · Antecedent associations.zip</strong> — analyse weather before sampling</summary>

Open the extracted folder containing `run_antecedent_analysis.py`. The runner reads `inputs/historical_daily_calendar.csv` from Step 4. It checks the rebuilt observations against `inputs/step5/previous_site_day_REFERENCE.csv` from the same-day analysis and `inputs/step5/current_modelling_dataset_REFERENCE.csv` from Step 5. All three are included.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe run_antecedent_analysis.py
```

Keep the complete `inputs` folder, including its 11 checksum-listed files. The runner rebuilds site-days from the workbook and checks them against both reference tables. Its lag models use rainfall on the three days before sampling. The seven-day rainfall and API predictors belong to the separate Step 5 prediction models. The runner records completion in `results/RUN_COMPLETION.json`.

</details>

## Moving from the observations to Steps 1–6

With the supplied files, continue to Step 1 after D. Step 1 already contains the historical classifications, rainfall workbook and family mapping it uses. You do not need to copy any files from A–D into Step 1.

If you also want to **regenerate the tables used by D**, run A–C, then Steps 1–5. Compare C’s site-day table, Step 4’s calendar and Step 5’s modelling table with the three copies listed under D. The D runner reads its own `inputs` folder. You can then run D and Step 6 independently. Step 4 calculates the seven-day wetness predictors used in the main workflow. D examines the preceding three days and can use its saved copies of the tables at any time.

<a id="main-analysis"></a>

## Step 1 · Build the historical weather baseline on Windows

1. With **Python 3.12** installed, open [Step1_publication_final.zip](./Step1_publication_final.zip) on GitHub and download the ZIP. This is the only package you need for Step 1.
2. In File Explorer, right-click the ZIP and choose **Extract All**. Open the extracted folder called **Step1_weather_baseline**. You are in the right place when you can see both `requirements.txt` and the `code` folder.
3. Click the File Explorer address bar, type `powershell` and press **Enter**. Run the following lines one at a time. The third command checks the results.

```powershell
py -3.12 -m pip install -r requirements.txt
py -3.12 code/step1_baseline.py
py -3.12 code/verify_saved_results.py
```

When the verifier finishes successfully, open `data/processed/weather_calendar.csv` to see the daily family assignments. Continue with Step 2.

## Continue through the main workflow

| Step | What to download or have ready |
| --- | --- |
| 2 · Check persistence and switching | [Step2_Markov_check.zip](./Step2_Markov_check.zip). Its copy of the Step 1 calendar is included. |
| 3 · Generate six storylines | [Step3_storylines_publication.zip](./Step3_storylines_publication.zip). It fits its own transitions. |
| 4 · Calculate weather and antecedent wetness | [Step4_GitHub.zip](./Step4_GitHub.zip) and the two source folders described under Step 4. |
| 5 · Fit the prediction models | [Step5_GitHub.zip](./Step5_GitHub.zip), [Step6_Part5.zip](./Step6_Part5.zip) and [Step6_Part7.zip](./Step6_Part7.zip). |
| 6 · Compare selected days, clusters and longest runs | All seven Step 6 parts extracted together. See the commands below. |

Click a step to show its commands. For Steps 2 and 3, extract the ZIP and open PowerShell in the named folder as you did for Step 1. For Steps 4–6, begin with the ZIPs in an empty working folder. The commands use the filenames shown here; remove duplicate-download suffixes such as `(1)` from the numbered step ZIPs first.

<details>
<summary><strong>2 · Step2_Markov_check.zip</strong> — check weather-family persistence and switching</summary>

Open `Step2_Markov_check`. The first script checks the Markov model against the historical calendar. The second writes the report.

```powershell
py -3.12 -m pip install -r requirements.txt
py -3.12 code/check_markov.py
py -3.12 code/report.py
```

Read `results/findings.txt` for the outcome of the checks.

</details>

<details>
<summary><strong>3 · Step3_storylines_publication.zip</strong> — generate six circulation storylines</summary>

Open `Step3_storylines`. This step fits transitions from its April–September classifications and generates 5,000 seasons per storyline.

```powershell
py -3.12 -m pip install -r requirements.txt
py -3.12 code/step3.py
py -3.12 code/report_step3.py
py -3.12 code/verify_results.py
```

The six simulated family sequences are saved in `results/primary_sequences_AprSep.npz`. The Step 4 input bundle already contains an identical copy.

</details>

<details>
<summary><strong>4 · Step4_GitHub.zip</strong> — add daily rainfall, meteorology and antecedent wetness</summary>

Put `Step4_GitHub.zip` in an empty folder called `Step4_work`. For the second ZIP, check **what is inside** the antecedent archive. The supplied `Antecedent(3).zip` includes a `Step4_final` folder with both `Step4_available_inputs` and `source_archives`. If your copy has both folders, put that ZIP in `Step4_work` and name the copy `Step4_inputs.zip`. If your GitHub copy contains only the observed lag analysis, you need the full API-corrected Step 4 archive or those two original input folders to run this step.

Open PowerShell in `Step4_work`. The commands below copy the two input folders into the compact package, then calculate historical and simulated daily weather. You can run Step 4 without running the separate antecedent-associations script.

```powershell
$ErrorActionPreference = 'Stop'
Expand-Archive -LiteralPath 'Step4_GitHub.zip' -DestinationPath .
Expand-Archive -LiteralPath 'Step4_inputs.zip' -DestinationPath '.\sources'
foreach ($folder in 'Step4_available_inputs', 'source_archives') {
    $target = New-Item -ItemType Directory -Force -Path ".\Step4_final\$folder"
    Copy-Item ".\sources\Step4_final\$folder\*" -Destination $target.FullName -Recurse -Force
}
Set-Location '.\Step4_final'
py -3.12 -m pip install -r requirements-lock.txt scipy
py -3.12 extract_sources.py
py -3.12 run_all.py --base-dir .
```

Step 4 needs SciPy as well as the packages in its lock file: the pre-run tests use xarray’s SciPy NetCDF engine. The run checks the restored input manifest. `verify_package.py` checks the inventory of the *complete original distribution*, so use it only with that distribution.

All 380 files listed in the restored inputs manifest and all 159 unpacked meteorological files were checked against their recorded hashes. The new run appears in a dated folder under `outputs`. Open `prepared/historical_daily_calendar.csv` there and look for `p7_mm`, `api` and `swvl1_roll` to see the historical wetness predictors. The `simulations` folder contains the six sets of donor sequences used to reconstruct wetness through each simulated season. [Step 4 guide](./README_Step4.md)

</details>

<details>
<summary><strong>5 · Step5_GitHub.zip</strong> — fit daily exceedance models and apply them to the storylines</summary>

Make an empty folder called `Step5_work`. Place **three ZIPs** in it: `Step5_GitHub.zip`, `Step6_Part5.zip` and `Step6_Part7.zip`. Parts 5 and 7 supply all 32 input files required by the Step 5 runner. You can start here using these saved inputs.

Open PowerShell in `Step5_work`. These commands extract the packages, copy the inputs into place and run the models.

```powershell
Expand-Archive -LiteralPath 'Step5_GitHub.zip' -DestinationPath .
Expand-Archive -LiteralPath 'Step6_Part5.zip' -DestinationPath .
Expand-Archive -LiteralPath 'Step6_Part7.zip' -DestinationPath .
Copy-Item '.\Step6_final\inputs\step5\inputs\*' '.\Step5_final\inputs\' -Recurse -Force
Set-Location '.\Step5_final'
py -3.12 -m pip install -r requirements.txt
py -3.12 run_step5.py
```

The runner rebuilds outcomes from the workbook, checks them against the frozen same-day site-day table, and prints its new run folder. Inside it, `results/performance_pooled.csv` contains the historical model scores, `fitted_models` contains the fitted models and calibrators, and `simulation_probabilities/selection_masks` records the selected days.

For the results check or additional publication plots, open the **completed new run folder**, which contains the held-out prediction files. Run `py -3.12 verify_results.py` or `py -3.12 code/plot_additional_publication_figures.py` there. The compact ZIP omits those prediction files. `verify_package.py` checks the original full inventory. [Step 5 guide](./README_Step5.md)

</details>

<a id="step-six-run"></a>

<details>
<summary><strong>6 · Step6_Part1.zip through Step6_Part7.zip</strong> — compare selected days, clusters and longest runs</summary>

The seven ZIPs form **one analysis**. To browse the saved storyline results, extract [Step6_Part1.zip](./Step6_Part1.zip) and open `Step6_final/START_HERE.html`. The numerical runner reads code, input checksums, four saved comparison tables and model inputs from Parts 1, 5, 6 and 7. Use all seven parts for the complete release, its saved draws and figure checks. Make an empty folder called `Step6_work` and place all seven ZIPs inside. Open PowerShell in `Step6_work`. Paste this block to extract the parts into one folder and install the dependencies:

```powershell
$ErrorActionPreference = 'Stop'
foreach ($part in 1..7) {
    Expand-Archive -LiteralPath "Step6_Part$part.zip" -DestinationPath .
}
Set-Location '.\Step6_final'
py -3.12 -m pip install -r requirements.txt
```

**To check the supplied results**, run `py -3.12 run_step6.py --verify-only`. This checks the existing results and figures. To repeat the numerical analysis from the inputs, the entry point is:

```powershell
py -3.12 rerun_step6_analysis.py
```

The runner requires a **new output directory**. Its default is `Step6_recalculated` alongside the extracted folder. For another attempt, use a fresh name, for example `py -3.12 rerun_step6_analysis.py --output ..\Step6_recalculated_02`.

**Original run.** Before the ZIP was split, the package recorded a successful fresh run of `rerun_step6_analysis.py`: 4,000 bootstrap replicates for each of the 11 models, 270 model comparisons and 190 storyline comparisons. The log records agreement with the delivered results. See `logs/api_fresh_reproduction.log` and `results/INDEPENDENT_REPRODUCTION.json` in Part 1. Across the seven parts, all 792 original files retain their paths and SHA-256 hashes. The added file is `README_GitHub.md`.

**Later reproducibility check.** All 121 input checksums passed in a separate Linux run using the pinned packages. The original code requires an exact match to the saved probability cutoff (`code/analysis_step6.py`, inside `run`). This run stopped at model H’s pooled top-1% cutoff before starting its bootstrap. Four of 55 cutoffs differed by at most 5.55 × 10⁻¹⁷. All 55 sets of selected days and their cutoff tie counts matched, as did all 360,000 seasonal records for the fixed 8- and 16-day selections. The saved-result verifier passed, and all 190 storyline contrasts were reproduced using the supplied draws for the pooled comparisons.

| Part | Contents |
| --- | --- |
| 1 | Analysis scripts, seasonal results, reports and publication figures |
| 2 | Saved bootstrap draws |
| 3 | Inference and supplementary figures |
| 4 | Additional and archived figures |
| 5 | Fitted models, simulated weather and upstream results |
| 6 | Records identifying the simulated days selected by each model |
| 7 | Historical inputs, including the bathing-water workbook |

[Step 6 guide](./README_Step6.md)

</details>

## Reproducibility checks

<details>
<summary><strong>Input provenance and wetness definitions</strong></summary>

Keep the Step 1 workbook and both `data/provenance/histogram_source_audit.json` and `data/provenance/histogram_source_status.csv`. The script checks the workbook’s hash. The extra source check, `py -3.12 code/audit_histogram_sources.py --eligible-only`, reads the nested `data/input/readable_histograms.zip`. A copy of that histogram ZIP also supplies Step 4.

The four-family weather calendar and daily rainfall summaries are in `data/processed`. Step 2 uses the calendar. Step 3 uses the rainfall summaries for diagnostics.

**Where antecedent wetness enters the workflow.** Steps 1–3 establish the weather-family baseline, check persistence and generate daily family sequences. **Step 4** attaches daily rainfall and soil moisture and calculates three predictors: seven-day rainfall total (`p7_mm`), antecedent precipitation index (`api`, decay factor 0.85) and seven-day mean top-layer soil moisture (`swvl1_roll`). April supplies the lead-in for May. The predictive seven-day total includes the current day. When choosing a historical donor, Step 4 can also use the preceding seven days of rainfall, excluding the current day (`p7_before_mm`).

**Step 5** uses the three wetness predictors in models F, G, H, J and K. The **full Step 6 rerun** reconstructs the simulated daily predictors from the saved donor days, reapplies the fitted models and compares runs of selected high-probability days. For a standalone Step 5 rerun, the historical wetness calendar is already in Step 6 Part 7, and Part 5 supplies the simulated donor sequences.

Across the CEDA archive and the readable-histogram archive in Step 1, 1,940 of the workbook’s 1,969 dates have a readable histogram. For the other 29 dates, 23 files are unreadable and six are absent. Use the bundled workbook to repeat the published family audit.

</details>

<details>
<summary><strong>What was tested</strong></summary>

| Package | Checks performed on fresh extracts |
| --- | --- |
| Prevalence and rainfall families | All seven prevalence CSVs matched the saved files. A regenerated rainfall-family audit passed all 31 checks. |
| Observed associations | Both sets of input checksums passed. The antecedent runner’s cohort and exposure calculations reproduced 35,518 site-days and all 32 exposure columns. The full observational model fits were not repeated. |
| Steps 1–3 | Steps 1 and 2 ran at their published settings and their key tables matched byte for byte. Step 3 passed a reduced end-to-end rerun and its verifier passed on the supplied full run. |
| Step 4 | Using the saved daily meteorology, reconstructed the 2,379-day calendar and 2,305-day donor library. Donor selections for the first three seasons matched in all six storylines. Raw NetCDF decoding was not repeated locally because xarray and netCDF4 were unavailable. |
| Step 5 | All 32 input checksums and all 10 packaged tests passed. Rebuilt 35,518 site-days and checked full-precision predictions for two baseline seasons across all 11 models against the stored predictions at their saved precision. Full model refitting was not repeated. |
| Step 6 | Saved-result verification and all 20 tests passed. Pooled selections and fixed-count records matched independently. The archived full rerun passed. The later numerical check stopped before its bootstrap, as described above. |

Runtime checks used Linux and Python 3.12. The PowerShell commands describe the Windows folder layout. One additional point for native Windows testing is temporary-file cleanup: both `Step5_final/code/storylines.py` and `Step6_final/code/analysis_step6.py` keep NumPy views of a memory-mapped probability array when calling `unlink()`. A native Windows end-to-end run was not tested here.

</details>
