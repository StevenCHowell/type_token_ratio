pyinstaller --noconfirm --clean --onefile \
            --distpath linux_app \
            -n ttr \
            --icon=ttr_icon.png \
            -p /home/schowell/data/myPrograms/anaconda3/envs/ttr35/lib/python3.5/site-packages/appJar/ \
            ./gui_ttr.py

# zip up the result
cd linux_app/
zip ttr.zip ttr
