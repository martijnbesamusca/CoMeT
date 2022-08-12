from collections import namedtuple
import subprocess


FloorplanConfig = namedtuple('FloorplanConfig', ['name', 'base', 'commandline_args'])

floorplan_dir = 'config/hotspot'
config_dir = 'config'

floorplans = [
    FloorplanConfig(
        name='gainestown_DDR_l3_stacked',
        base='gainestown_DDR',
        commandline_args=[
            '--mode', 'DDR',
            '--cores', '2x2', '--corex', '3.414mm', '--corey', '3.414mm',
            '--banks', '4x4', '--bankx', '1.707mm', '--banky', '1.707mm',
            '--cache_L3', 'stacked', '--cachex', '6.828mm', '--cachey', '6.828mm',
        ]
    ),
    FloorplanConfig(
        name='gainestown_DDR_l3_non-stacked',
        base='gainestown_DDR',
        commandline_args=[
            '--mode', 'DDR',
            '--cores', '2x2', '--corex', '3.414mm', '--corey', '3.414mm',
            '--banks', '4x4', '--bankx', '1.707mm', '--banky', '1.707mm',
            '--cache_L3', 'non-stacked', '--cachex', '6.828mm', '--cachey', '6.828mm',
        ]
    ),
    FloorplanConfig(
        name='gainestown_3Dmem_l3_stacked',
        base='gainestown_3Dmem',
        commandline_args=[
            '--mode', '3Dmem',
            '--cores', '2x2', '--corex', '3.414mm', '--corey', '3.414mm',
            '--banks', '4x4x8', '--bankx', '1.707mm', '--banky', '1.707mm',
            '--cache_L3', 'stacked', '--cachex', '6.828mm', '--cachey', '6.828mm',
        ]
    ),
    FloorplanConfig(
        name='gainestown_3Dmem_l3_non-stacked',
        base='gainestown_3Dmem',
        commandline_args=[
            '--mode', '3Dmem',
            '--cores', '2x2', '--corex', '3.414mm', '--corey', '3.414mm',
            '--banks', '4x4x8', '--bankx', '1.707mm', '--banky', '1.707mm',
            '--cache_L3', 'non-stacked', '--cachex', '6.828mm', '--cachey', '6.828mm',
        ]
    ),
    FloorplanConfig(
        name='gainestown_2_5D_l3_stacked',
        base='gainestown_2_5D',
        commandline_args=[
            '--mode', '2.5D',
            '--cores', '2x2', '--corex', '3.415mm', '--corey', '3.415mm',
            '--banks', '4x4x8', '--bankx', '1.707mm', '--banky', '1.707mm',
            '--core_mem_distance', '1.3mm',
            '--cache_L3', 'stacked', '--cachex', '6.83mm', '--cachey', '6.83mm',
        ]
    ),
    FloorplanConfig(
        name='gainestown_2_5D_l3_non-stacked',
        base='gainestown_2_5D',
        commandline_args=[
            '--mode', '2.5D',
            '--cores', '2x2', '--corex', '3.415mm', '--corey', '3.415mm',
            '--banks', '4x4x8', '--bankx', '1.707mm', '--banky', '1.707mm',
            '--core_mem_distance', '1.3mm',
            '--cache_L3', 'non-stacked', '--cachex', '6.83mm', '--cachey', '6.83mm',
        ]
    ),
    FloorplanConfig(
        name='gainestown_3D_l3_stacked',
        base='gainestown_3D',
        commandline_args=[
            '--mode', '3D',
            '--cores', '2x2', '--corex', '3.414mm', '--corey', '3.414mm',
            '--banks', '4x4x8', '--bankx', '1.707mm', '--banky', '1.707mm',
            '--cache_L3', 'stacked', '--cachex', '6.828mm', '--cachey', '6.828mm',
        ]
    ),
    FloorplanConfig(
        name='gainestown_3D_l3_non-stacked',
        base='gainestown_3D',
        commandline_args=[
            '--mode', '3D',
            '--cores', '2x2', '--corex', '2.276mm', '--corey', '3.414mm',
            '--banks', '4x4x8', '--bankx', '1.707mm', '--banky', '1.707mm',
            '--cache_L3', 'non-stacked', '--cachex', '2.276mm', '--cachey', '6.828mm',
        ]
    ),
    # 16 core
    # FloorplanConfig(
    #     name='gainestown_DDR_16core_l3_stacked',
    #     base='gainestown_DDR_16core',
    #     commandline_args=[
    #         '--mode', 'DDR',
    #         '--cores', '4x4', '--corex', '2.876mm', '--corey', '2.876mm',
    #         '--banks', '4x4', '--bankx', '1.707mm', '--banky', '1.707mm',
    #         '--cache_L3', 'stacked', '--cachex', '11.504mm', '--cachey', '11.504mm',
    #     ]
    # ),
    # FloorplanConfig(
    #     name='gainestown_DDR_16core_l3_non-stacked',
    #     base='gainestown_DDR_16core',
    #     commandline_args=[
    #         '--mode', 'DDR',
    #         '--cores', '4x4', '--corex', '2.876mm', '--corey', '2.876mm',
    #         '--banks', '4x4', '--bankx', '1.707mm', '--banky', '1.707mm',
    #         '--cache_L3', 'non-stacked', '--cachex', '2.876mm', '--cachey', '11.504mm',
    #     ]
    # ),
    # FloorplanConfig(
    #     name='gainestown_3Dmem_16core_l3_stacked',
    #     base='gainestown_3Dmem_16core',
    #     commandline_args=[
    #         '--mode', '3Dmem',
    #         '--cores', '4x4', '--corex', '2.876mm', '--corey', '2.876mm',
    #         '--banks', '4x4x8', '--bankx', '1.707mm', '--banky', '1.707mm',
    #         '--cache_L3', 'stacked', '--cachex', '11.504mm', '--cachey', '11.504mm',
    #     ]
    # ),
    # FloorplanConfig(
    #     name='gainestown_3Dmem_16core_l3_non-stacked',
    #     base='gainestown_3Dmem_16core',
    #     commandline_args=[
    #         '--mode', '3Dmem',
    #         '--cores', '4x4', '--corex', '2.876mm', '--corey', '2.876mm',
    #         '--banks', '4x4x8', '--bankx', '1.707mm', '--banky', '1.707mm',
    #         '--cache_L3', 'non-stacked', '--cachex', '2.876mm', '--cachey', '11.504mm',
    #     ]
    # ),
    # FloorplanConfig(
    #     name='gainestown_2_5D_16core_l3_stacked',
    #     base='gainestown_2_5D_16core',
    #     commandline_args=[
    #         '--mode', '2.5D',
    #         '--cores', '4x4', '--corex', '2.876mm', '--corey', '2.876mm',
    #         '--banks', '4x4x8', '--bankx', '1.707mm', '--banky', '1.707mm',
    #         '--core_mem_distance', '3mm',
    #         '--cache_L3', 'stacked', '--cachex', '11.504mm', '--cachey', '11.504mm',
    #     ]
    # ),
    # FloorplanConfig(
    #     name='gainestown_2_5D_16core_l3_non-stacked',
    #     base='gainestown_2_5D_16core',
    #     commandline_args=[
    #         '--mode', '2.5D',
    #         '--cores', '4x4', '--corex', '2.876mm', '--corey', '2.876mm',
    #         '--banks', '4x4x8', '--bankx', '1.707mm', '--banky', '1.707mm',
    #         '--core_mem_distance', '3mm',
    #         '--cache_L3', 'non-stacked', '--cachex', '2.876mm', '--cachey', '11.504mm',
    #     ]
    # ),
    # FloorplanConfig(
    #     name='gainestown_3D_16core_l3_stacked',
    #     base='gainestown_3D_16core',
    #     commandline_args=[
    #         '--mode', '3D',
    #         '--cores', '4x4', '--corex', '2mm', '--corey', '2mm',
    #         '--banks', '4x4x8', '--bankx', '2mm', '--banky', '2mm',
    #         '--cache_L3', 'stacked', '--cachex', '8mm', '--cachey', '8mm'
    #     ]
    # ),
    # FloorplanConfig(
    #     name='gainestown_3D_16core_l3_non-stacked',
    #     base='gainestown_3D_16core',
    #     commandline_args=[
    #         '--mode', '3D',
    #         '--cores', '4x4', '--corex', '2mm', '--corey', '2mm',
    #         '--banks', '4x4x8', '--bankx', '2.5mm', '--banky', '2mm',
    #         '--cache_L3', 'non-stacked', '--cachex', '2mm', '--cachey', '8mm'
    #     ]
    # ),
]

def generate_floorplans():
    for name, base, args in floorplans:
        args += ['--out', f'../../{floorplan_dir}/{name}']
        print(name)
        try:
            output = subprocess.check_output(['python3', '../../floorplanlib/create.py'] + args, stderr=subprocess.STDOUT)

        except subprocess.CalledProcessError as e:
            print(f'ERROR (call failed)')
            for line in e.output.decode('utf-8').splitlines():
                print(f'   {line}')
            continue

def generate_configs():
    cores = 4
    for name, base, args in floorplans:
        n = 'mem' if '3Dmem' in name or 'DDR' in name else 'stack'
        template = f'''\
#include {base}.cfg
[core_power]
l3 = true

[perf_model/cache]
levels = 3

[perf_model/dram]
num_controllers = -1
controllers_interleaving = {cores}

[perf_model/l3_cache]
shared_cores = {cores}
dvfs_domain = global

[hotspot]
floorplan_folder = {floorplan_dir}/{name}
init_file_external_mem = None
hotspot_config_file_mem  =  {floorplan_dir}/{name}/{n}_hotspot.config
layer_file_mem = {floorplan_dir}/{name}/{n}.lcf
# only used for DDR and 3Dmem
init_file_external_core = None
hotspot_config_file_core  =  {floorplan_dir}/{name}/cores_hotspot.config
layer_file_core  =   {floorplan_dir}/{name}/cores.lcf
'''
        with open(f"../../{config_dir}/{name}.cfg", "w") as file:
            file.write(template)


generate_floorplans()
generate_configs()