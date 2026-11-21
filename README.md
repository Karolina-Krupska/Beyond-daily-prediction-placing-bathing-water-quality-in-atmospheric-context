[README.md](https://github.com/user-attachments/files/35217343/README.md)
# Beyond-daily-prediction-placing-bathing-water-quality-in-atmospheric-context

This analysis links weather patterns, radar rainfall and environmental conditions to intestinal enterococci exceedances at monitored bathing waters during May-September 2012-2024. The observational analyses address which conditions accompanied exceedances and whether weather patterns improved daily prediction. The storyline experiments examine how model-selected days cluster across simulated seasons.

Start with radar processing and radar quality checks. Then follow weather pattern prevalence, rainfall families, observed exceedance associations and antecedent analysis. The six numbered steps follow in their original order. Each package includes the processed inputs for its published analysis, so you can also reproduce an individual result directly.

If you have the twelve original ZIPs, use the filenames in the table. If you have the two larger delivery ZIPs, the six supporting packages and Step 6 are in `Bathing_Water_Step_6_and_Other_Analyses.zip`. Steps 1 to 5 are in `Bathing_Water_Steps_1_to_5.zip`. Extract the individual ZIP before running a script. `FILE_INDEX.csv` lists the files in all twelve packages.

## Packages in reading order

| Analysis | Original ZIP filename | Main script or contents |
| --- | --- | --- |
| Radar processing | `CEDA processing file and data(8).zip` | `All reg log2 and linear 2016 1.py` |
| Radar quality checks | `CEDA data QA notes(4).zip` | Two Word documents describing radar QA |
| Weather pattern prevalence | `weather_pattern_prevalence_publication (1)(8).zip` | `prevalence_publication.py` |
| Rainfall families | `SWEW_rainfall_families_publication_v1_0(20261120-130931).zip` | `code/01_weather_pattern_family_mapping.py` |
| Exceedance associations | `SWEW_exceedance_associations (1)(10).zip` | `code/bathing_water_exceedance_associations.py` |
| Antecedent analysis | `Antecedent associations(6).zip` | `run_antecedent_analysis.py` |
| Step 1 | `Step1_publication_final(6).zip` | `code/step1_baseline.py` |
| Step 2 | `Step2_Markov_check(6).zip` | `code/check_markov.py` |
| Step 3 | `Step3_storylines_publication(8).zip` | `code/step3.py` |
| Step 4 | `Step4_final(9).zip` | `extract_sources.py`, then `run_all.py --base-dir .` |
| Step 5 | `Step5_final (2)(9).zip` | `run_step5.py` |
| Step 6 | `Step6_final(6).zip` | `run_step6.py` |

## Set up Python and IDLE

1. Extract the ZIP for the analysis you want into a fresh, writable folder. Keep its internal directories together. The prevalence ZIP has files at its top level, so give it a folder of its own. The table above gives the exact archive names.
2. On Windows, open the extracted **package folder** in File Explorer, type `cmd` in its address bar and press Enter. For Step 1, this is `Step1_weather_baseline`, the folder containing `code` and `requirements.txt`. Keep the original ZIP so you can return to the supplied results.
3. In **Command Prompt**, create and activate a Python 3.12 environment for that package. The commands below use the Windows Python launcher.

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

For a package with `requirements.txt`, run `python -m pip install -r requirements.txt` before running its analysis. For Step 4, use `python -m pip install -r requirements-lock.txt` for the recorded versions. The radar and prevalence packages use the short installation commands in their sections. The radar QA documents need no installation. Separate environments preserve the dependency versions requested by each package.

**If you use IDLE**, enter `python -m idlelib` in that same activated Command Prompt. In IDLE choose **File > Open**, select the entry script, then **Run > Run Module (F5)**. For example, open `run_step6.py` to reproduce the final storyline comparisons, or `make_figures_only.py` in the antecedent package to redraw its figures. When a command below includes arguments such as `--verify-only` or `--base-dir .`, the simplest option is to paste the whole line into the activated Command Prompt. A plain F5 uses the script's defaults.

On macOS or Linux, the equivalent setup is `python3.12 -m venv .venv`, followed by `source .venv/bin/activate`. Run each block below from its named package folder, one command at a time. Use a working copy for regeneration because some scripts refresh existing figures, reports or verification files.

## Supporting analyses and data preparation

### Radar processing

The later packages include the processed rainfall inputs they use. To start from raw radar instead, use `CEDA processing file and data`. Supply the original daily NIMROD `.tar` archives and set `base_dir` inside the main block of a working copy of `All reg log2 and linear 2016 1.py` to the directory containing them. The program reads TARs directly inside that directory. Run it for each input directory if the files are arranged by year.

```bash
python -m pip install numpy pyproj
python "All reg log2 and linear 2016 1.py"
```

The script writes dated regional rainfall-rate histograms to the current working directory. The raw TARs are external to these twelve packages. The rainfall family analysis starts from its supplied processed workbook, which includes records beyond those reconstructable from the retained histogram files.

### Radar quality checks

Open the folder `CEDA data QA notes` and read the two supplied documents:

- `Radar_rainfall_QC_supplementary_section.docx`
- `Radar_rainfall_QC_supplement_and_review_notes.docx`

They document the coverage and anomaly checks. This package has no Python entry point. For the executable audit that reconstructs eligible rainfall records from retained histograms, use `python code/audit_histogram_sources.py --eligible-only` in Step 1.

### Weather pattern prevalence

In the folder containing `prevalence_publication.py`, use the supplied classification CSV explicitly. This overrides the original computer's default input path.

```bash
python -m pip install numpy pandas matplotlib
python prevalence_publication.py --input "classifications_30regimes(21) (4).csv" --output reproduced_prevalence
```

Compare `reproduced_prevalence/monthly_prevalence_percent.csv` with the copy in `results/`. Monthly prevalence describes how often each pattern occurred. Daily classifications retain the sequence needed for the Markov analysis.

### Rainfall families

From `SWEW_rainfall_families`, reproduce the mapping from the supplied SWEW rainfall workbook, regenerate the displays and publication tables, then check the saved package results.

```bash
python code/01_weather_pattern_family_mapping.py --csv-only
python code/02_plot_saved_rainfall_summaries.py
python code/04_export_publication_tables.py
python code/03_verify_results.py --package .
```

The regenerated mapping is under `results/reproduced_family_mapping/`. Omit `--csv-only` to produce the Excel audit as well. The published lookup is `results/family_mapping/publication_family_mapping.csv`. Use the reviewed `group_final4` field to map the 30 weather patterns to four rainfall process families.

### Exceedance associations

From `SWEW_bathing_water_associations`, run the site-day analysis using the included monitoring workbook, weather calendar and family lookup. The following commands write the analysis to a separate folder and verify that output.

```bash
python -m unittest discover -s code -v
python code/bathing_water_exceedance_associations.py --output reproduced_associations
python code/verify_results.py --output reproduced_associations
```

Open `reproduced_associations/models/` for the observed-data association estimates and `reproduced_associations/figure_data/` for the values used in figures. To redraw just the combined family figure from the saved results, run `python code/plot_family_combined.py` in the working copy.

### Antecedent analysis

It uses historical site-days, the weather calendar and family mapping included in `Antecedent associations`. It can run independently of the storyline experiments.

| Purpose | Command from `Antecedent associations` |
| --- | --- |
| Redraw figures from the saved tables | `python make_figures_only.py` |
| Rebuild the cohort, fit the models, run the 2,000 paired whole-year refits and produce the figures and verification | `python run_antecedent_analysis.py` |

Both scripts support IDLE **F5**. The combined figure is `figures/Figure_Combined_Circulation_and_Rainfall.pdf`. Its heatmaps describe family occurrence around observed exceedances, while the fitted comparison asks whether preceding Cyclonic Atlantic days retain an association after rainfall adjustment. Read `FIGURE_INDEX.md` for the plotted sources and `results/RUN_COMPLETION.json` for the full-run status. If Windows cannot start the bootstrap workers, the package supports setting `bootstrap_workers` to `1` in the working copy of `config.json`.

## Main analytical procedure

Follow Steps 1 to 6 in numerical order for the full procedure. A later package uses the upstream files already bundled with it. Running an earlier stage does not automatically replace those files.

### Step 1. Describe the historical baseline

From `Step1_weather_baseline`, run the baseline analysis followed by its checks.

```bash
python code/step1_baseline.py
python code/test_step1.py
python code/test_uncertainty.py
python code/verify_saved_results.py
python code/audit_histogram_sources.py --eligible-only
```

The daily circulation calendar contains 1,989 classified summer days. Rainfall summaries use the 1,940 days with reconstructable histograms. Step 2 uses the calendar in `data/processed/weather_calendar.csv`. Steps 3 and 4 include copies of the retained rainfall table, `data/processed/daily_metrics_SWEW_MaySep_NOQC.csv`. For figures alone, run `python code/plot_step1.py`.

### Step 2. Check the Markov generator

From `Step2_Markov_check`, compare simulated persistence and switching with the observed May-September family sequences, including held-out summers.

```bash
python code/test_check.py
python code/check_markov.py
python code/report.py
```

Read `results/matched_horizon_check.csv` and `results/heldout_season_check.csv`. The report command alone recreates the displays from saved results. This step evaluates the pooled and monthly generators. Step 3 fits the generator for its own April-September simulation window.

### Step 3. Generate circulation storylines

From `Step3_storylines`, use the daily classifications and bundled summer rainfall diagnostic to reproduce the circulation experiments.

```bash
python code/test_step3.py
python code/step3.py
python code/report_step3.py
python code/verify_results.py
```

The default run produces 5,000 seasons for the baseline and for each of five alternative storylines. Each season includes 30 April warm-up days and 153 May-September evaluation days. Step 4 uses the family sequences saved in `results/primary_sequences_AprSep.npz`. To regenerate the figures from saved results, run `python code/report_step3.py` alone.

### Step 4. Attach daily environmental conditions

From `Step4_final`, check the delivered files, unpack the six included meteorological source archives and run the driver reconstruction.

```bash
python verify_package.py
python extract_sources.py
python run_all.py --base-dir .
```

**Keep the final dot.** It points the workflow to the extracted package on your computer. The code selects historical donor days for the simulated family and month and recalculates antecedent wetness along each sequence. It also runs the prescribed sensitivity and held-out checks.

The delivered summaries are in `completed_run/results/ensemble_summary.csv` and the figures in `completed_run/figures/`. A fresh run writes to `outputs/Step4_<timestamp>/`. Check its `run_metadata.json` and `results/assessment_completion.json`. To export daily CSV files from the delivered compact data, run `python export_daily.py completed_run`.

### Step 5. Evaluate daily exceedance predictions

From `Step5_final`, check the delivered files and predictions first.

```bash
python verify_package.py
python -m unittest discover -s code -p "test*.py" -v
python verify_results.py
```

To **refit the models and reproduce the full predictive analysis**, run:

```bash
python run_step5.py
```

This fits models A-K, evaluates each on held-out years, calibrates probabilities using the training years and runs the sensitivity analyses. It also compares the held-out predictions using 4,000 whole-year bootstrap samples. Finally, it fits models to the complete observed dataset and applies them to the supplied Step 4 drivers. With the delivered completion record present, the default command writes a new `runs/Step5_<timestamp>/` folder. Reserve `--resume` for an interrupted working copy with the same inputs and settings.

Open `results/performance_pooled.csv`, `results/performance_by_year.csv` and `results/paired_bootstrap_intervals.csv` for the historical predictive evaluation. The model definitions are in `model_registry.json`. Two optional commands use saved outputs:

```bash
python code/plot_additional_publication_figures.py --output figures_redrawn
python export_probabilities.py --scenario baseline --n-seasons 2
```

The first redraws the two additional publication figures. The second exports two baseline seasons. For exact Step 5 selections use `selection_masks/`, since the distributed probability arrays are rounded to float32.

### Step 6. Compare the seasonal organisation of model-selected days

From `Step6_final`, choose **one** of these routes.

| Purpose | Command or file |
| --- | --- |
| Read existing results, figures and captions | Open `START_HERE.html`. |
| Check the saved analysis | Run `python run_step6.py --verify-only`. This also refreshes reports, verification records and a log. |
| Reproduce the current storyline comparisons and their figures | Run `python run_step6.py`, or open this file in IDLE and press **F5**. |

The active launcher uses saved result tables and bootstrap draws. The fitted models, calibration and simulated weather remain fixed. You can start directly here with the complete Step 6 package.

| Scientific question | Saved result |
| --- | --- |
| What changes when weather patterns are added to otherwise matched models? | `results/inference/paired_tests.csv` contains 270 between-model contrasts for E-C, F-J and G-K. The selected figures are in `figures/Publication_selection/`. |
| How does each storyline differ from baseline within model G or K? | `results/storyline_inference/all_contrasts.csv` contains 150 pooled and 40 equal-count contrasts, adjusted together as a separate family of 190 tests. Figures are in `figures/Storyline_comparisons/`. |

The main pooled Top 10% selects the highest-ranked 10% of days across all six scenarios for each model, allowing the count to vary between seasons and storylines. The other fractions are 1%, 5%, 25% and 50%. The equal-count check selects exactly 8 or 16 days in each 153-day season to compare **selected-day clusters** and **maximum run length** at a common count. Simulation intervals refer to Monte Carlo uncertainty conditional on the fitted system. The 5th-95th percentile seasonal ranges describe variation between seasons.

Check `results/storyline_inference/INDEPENDENT_VERIFICATION.json` and `FIGURE_VERIFICATION.json` in the same folder. The corresponding Methods and Results are in `reports/storyline_amendment/`.

## Reproducibility checks

All twelve distributed ZIPs match the SHA-256 digests recorded for the source packages. In the earlier documentation check, all 23 files in Step 5’s bundled Step 4 input directory and all 114 files in Step 6’s bundled Step 5 input directory matched their upstream copies by SHA-256. The Step 6 verification-only command passed its numerical checks, figure-source checks and 20 unit tests on an extracted copy under Python 3.12. The complete scientific workflow and the Windows IDLE interface were not rerun when assembling this release.
