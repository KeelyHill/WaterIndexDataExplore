# data clean

python3 extract_from_pdf.py
python3 clean_table.py

echo "Process..."

python3 pivot.py

python3 merge.py

# plots
echo "Plot..."
python3 plot_nutrient_per_water_chart.py
python3 plot_scatter_compare.py
python3 plot_heatmap_compare.py

echo "Complete\!"
