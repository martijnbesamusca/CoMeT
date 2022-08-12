import datetime
from sqlite3 import Timestamp
import runlib
import resultlib
import config
import os

def example2():
    for benchmark in (
                      'parsec-blackscholes',
                      #'parsec-bodytrack',
                      #'parsec-canneal',
                      #'parsec-dedup',
                      #'parsec-fluidanimate',
                      #'parsec-streamcluster',
                      #'parsec-swaptions',
                      #'parsec-x264',
                      #'splash2-barnes',
                      #'splash2-fmm',
                      #'splash2-ocean.cont',
                      #'splash2-ocean.ncont',
                      #'splash2-radiosity',
                      #'splash2-raytrace',
                      #'splash2-water.nsq',
                      #'splash2-water.sp',
                      #'splash2-cholesky',
                      #'splash2-fft',
                      #'splash2-lu.cont',
                      #'splash2-lu.ncont',
                      #'splash2-radix'
                      ):
        min_parallelism = runlib.get_feasible_parallelisms(benchmark)[0]
        max_parallelism = runlib.get_feasible_parallelisms(benchmark)[-1]
        for freq in (1, 2, 3, 4):
            for parallelism in (min_parallelism, max_parallelism):
                # you can also use try_run instead
                runlib.run(['open', '{:.1f}GHz'.format(freq), 'constFreq'], runlib.get_instance(benchmark, parallelism, input_set='simsmall'))


def example():
    for freq in (1, 2, 3, 4):  # when adding a new frequency level, make sure that it is also added in base.cfg
        runlib.run(['open', '{:.1f}GHz'.format(freq), 'constFreq'], 'parsec-blackscholes-simmedium-15')


def case_study():
    run_folder = os.path.join(config.RESULTS_FOLDER, f'runs-{runlib.BATCH_START}')
    os.mkdir(run_folder)

    arch_types = ['DDR', '3Dmem', '2.5D','3D'][::-1]
    L3_types = [None, 'stacked', 'non-stacked']
    for arch_type in arch_types:
        for L3_type in L3_types:
            sniper_config = 'gainestown_' + arch_type.replace('.', '_')
            print('\n'*2 + '-'*10 + 'Running: ' + sniper_config + '-'*10  + '\n'*2)
            if L3_type is not None:
                sniper_config += '_l3_' + L3_type
            config.modify_all({
                'SNIPER_CONFIG': sniper_config,
                'ARCH_TYPE': arch_type,
                'VIDEO_L3': L3_type is not None,
                'VIDEO_L3_STACKED': L3_type == 'stacked',
                'NUMBER_MEM_BANKS_Z': 1 if arch_type == 'DDR' else 8
                
            })
            run = runlib.try_run(['open', 'ondemand'], runlib.get_instance('parsec-swaptions', parallelism=4, input_set='medium'))
            if run:
                new_name = sniper_config
                os.rename(os.path.join(config.RESULTS_FOLDER, run), os.path.join(run_folder, new_name))
            print('DONE!')
            print('\a', end=None)
    print('\n'*2 + 'Done - All results in ' + f'results/runs-{runlib.BATCH_START}')

def recreate_videos(time_stamp):
    run_folder = os.path.join(config.RESULTS_FOLDER, f'runs-{runlib.BATCH_START}')
    arch_types = ['DDR', '3Dmem', '2.5D','3D']
    L3_types = [None, 'stacked', 'non-stacked']
    for arch_type in arch_types:
        for L3_type in L3_types:
            sniper_config = 'gainestown_' + arch_type.replace('.', '_')
            print('\n'*2 + '-'*10 + 'Running: ' + sniper_config + '-'*10  + '\n'*2)
            if L3_type is not None:
                sniper_config += '_l3_' + L3_type
            config.modify_all({
                'SNIPER_CONFIG': sniper_config,
                'ARCH_TYPE': arch_type,
                'VIDEO_L3': L3_type is not None,
                'VIDEO_L3_STACKED': L3_type == 'stacked',
                'NUMBER_MEM_BANKS_Z': 1 if arch_type == 'DDR' else 8
                
            })
            run = f'runs-{time_stamp}/{sniper_config}'
            # runlib.create_plots(run, True)
            runlib.create_video(run)


def main():
    # case_study()
    recreate_videos('2022-06-22_09.56')


if __name__ == '__main__':
    main()
