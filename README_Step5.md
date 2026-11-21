# Step 5 - Daily bathing water exceedance predictions

Step 5 tests whether weather patterns improve daily predictions of intestinal enterococci exceedance in South West England. It compares 11 models (A-K) using monitoring data from 2012-2024, holding out one year at a time for evaluation. It then applies the fitted models to the six simulated scenarios used in Step 6.

## Open the data, results and figures

1. Download and extract the repository ZIP, or download the Step 5 files individually. Keep all 17 parts (`step5-001.bin` to `step5-017.bin`), `manifest.json` and `restore_zip.py` together in one folder.
2. In Python IDLE, choose **File > Open**, open `restore_zip.py` and press **F5**. Choose a folder for the restored ZIP. The script checks each part and confirms when the complete ZIP is ready.
3. In Windows File Explorer, right-click the restored ZIP, choose **Extract All**, then open `Step5_final`. If you already have the complete original ZIP, start at this step.

| To find | Open |
| --- | --- |
| Bathing water observations | `inputs/bathing_water_records_2012_2024.xlsx` |
| Historical and simulated weather inputs from Step 4 | `inputs/step4/` |
| Daily model performance | `results/performance_pooled.csv` and `results/performance_by_year.csv` |
| Added value of weather patterns in the three model comparisons | `results/paired_bootstrap_intervals.csv` |
| Daily probabilities for the six simulated scenarios | `simulation_probabilities/` |
| Saved figures | `figures/` |

## Rerun the analysis in Windows IDLE

The archive includes the inputs needed from earlier steps. To view the saved results, simply open the files above. To rerun Step 5, use Python 3.12 and the single entry script, `run_step5.py`.

1. Open the extracted `Step5_final` folder in File Explorer. Type `cmd` in the address bar and press **Enter**.
2. In the command window, enter these lines one at a time. The first two set up the Python environment on your first run. The third opens the analysis script in IDLE.

   ```bat
   py -3.12 -m venv .venv
   .venv\Scripts\python.exe -m pip install -r requirements.txt
   .venv\Scripts\python.exe -m idlelib -e run_step5.py
   ```

3. In the IDLE editor, press **F5**. A fresh run from the supplied package writes its outputs to a dated folder under `runs/`. When it finishes, the IDLE shell displays `ALL STEP 5 TASKS COMPLETED`.
