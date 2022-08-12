TARGET=test
include ../shared/Makefile.shared

# CONFIG=gainestown_DDR
# CONFIG=gainestown_DDR_l3_stacked
# CONFIG=gainestown_DDR_l3_non-stacked # no writes?

# CONFIG=gainestown_3Dmem_l3_stacked
# CONFIG=gainestown_3Dmem_l3_non-stacked

#CONFIG=gainestown_2_5D
CONFIG=gainestown_2_5D_l3_stacked
# CONFIG=gainestown_2_5D_l3_non-stacked

# CONFIG=gainestown_3D
# CONFIG=gainestown_3D_l3_stacked
# CONFIG=gainestown_3D_l3_non-stacked

CFLAGS=-O0 -std=c99 $(SNIPER_CFLAGS)

$(TARGET): $(TARGET).o
	$(CC) $(TARGET).o -lm $(SNIPER_LDFLAGS) -o $(TARGET)

configs:
	# python3 architectures.py

run_$(TARGET): configs
	../../run-sniper -v -s memTherm_core -n 4 -c $(CONFIG) -- ./$(TARGET) -p 4

plot:
	../../scripts/heatView.py --plot_type 3D --arch_type 2.5D --tmin 45 --tmax 75 --banks_in_z 8 --cache_l3 --cache_l3_stacked --cache_l3_width 0 --traceFile combined_temperature.trace
	# ../../scripts/heatView.py --plot_type 3D --arch_type DDR --tmin 45 --tmax 75 --banks_in_z 1 --cache_l3 --cache_l3_width 1 --traceFile combined_temperature.trace

CLEAN_EXTRA=viz hotspot/ *.log *.init energystats-temp.* *.trace tmp *.cfg hotspot/* config/*