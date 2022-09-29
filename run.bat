rem pytest -v -s  -m "sanity" --browser firefox --html=Reports\report_sanity.html  --capture=tee-sys .\testcases\
rem pytest -v -s  -m "sanity" --browser chrome --html=Reports\report_sanity.html  --capture=tee-sys .\testcases\
pytest -v -s  -m "regression" --browser firefox --html=Reports\report_regression.html  --capture=tee-sys .\testcases\
REM pytest -v -s  -m "sanity and regression" --browser firefox --html=Reports\report_sanity.html  --capture=tee-sys .\testcases\
REM pytest -v -s  -m "sanity or regression" --browser firefox --html=Reports\report_sanity.html  --capture=tee-sys .\testcases\
