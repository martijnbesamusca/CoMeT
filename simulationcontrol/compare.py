import resultlib
import os
import numpy as np
import config
import matplotlib.pyplot as plt

def L3Type(run):
    with resultlib._open_file(run, 'sim.info') as f:
        for line in f.readlines():
            if 'l3_stacked' in line:
                return 'Stacked'
            if 'l3_non-stacked' in line:
                return 'Non-Stacked'
    return 'No'

def compare_runs(runs, name, ylabel, function, arch, directory=None, ylim=None):
    fig = plt.figure()
    for run in runs:

        label = f'{L3Type(run)} L3'
        trace = function(run)
        xs = range(len(trace))
        plt.plot(xs, trace, label=label)

    plt.xlabel('Time (ms)')
    plt.ylabel(f'{ylabel}')
    plt.grid()
    plt.grid(which='minor', linestyle=':')
    plt.minorticks_on()
    if ylim: plt.ylim(ylim)
    plt.legend()
    fn = f'compare_{arch}_{name}.svg'
    if directory:
        fn = os.path.join(directory, fn)
    plt.savefig(fn)
    plt.close()

def print_average(runs, name, function):
    for run in runs:
        trace = function(run)
        avg = np.average(trace)
        name = f'{L3Type(run)} L3'
        print(f'{name} | {avg}')

def save_time(runs, arch, directory=None):
    fn_out = f'perf_{arch}.tex'
    if directory:
        fn_out = os.path.join(directory, fn_out)
        
    with open(fn_out, 'w') as f_out:
        f_out.write('L3 Type & Time (ms) \n')
        f_out.write('\\\\ \\hline\\hline\n')
        for run in runs:
            fn = os.path.join(run, 'sim.out')
            with open(fn) as simout:
                for _ in range(4): simout.readline()
                data = simout.readline().split('|')
                assert('Time (ns)' in data[0])
                time = f'{int(data[1])/1000000:.4f}'
                l3 = f'{L3Type(run)} L3'
                f_out.write(f'{l3} & {time} \n')
                f_out.write('\\\\ \\hline\n')


def save_average(runs, name, function, arch, directory=None):
    name = f'average_{arch}_{name}'
    fn_out = name
    if directory:
        fn_out = os.path.join(directory, fn_out + '.tex')
        
    with open(fn_out, 'w') as f_out:
        f_out.write(f'#{name}\n')
        f_out.write(f'L3 Type & Average \n')
        f_out.write('\\\\ \\hline\\hline\n')
        for run in runs:
            trace = function(run)
            avg = np.average(trace)
            l3 = f'{L3Type(run)} L3'
            f_out.write(f'{l3} & {avg}\n')
            f_out.write('\\\\ \\hline\n')


def main(name):
    temps_lim = (40,100)
    arch_types = ['DDR', '3Dmem', '2.5D','3D']
    L3_types = ['', '_l3_stacked', '_l3_non-stacked']
    for arch_type in arch_types:
        directory = os.path.join(config.RESULTS_FOLDER, name)
        runs = [os.path.join(config.RESULTS_FOLDER, name, f"gainestown_{arch_type.replace('.', '_')}{L3_type}") for L3_type in L3_types]
        l3_runs = runs[1:]
        print(f'Arch types: {arch_type}')

        save_time(runs, arch=arch_type, directory=directory)

        save_average(runs, 'core_temp', lambda run: np.average(resultlib.get_core_temperature_traces(run), axis=0), arch=arch_type, directory=directory)
        save_average(runs, 'mem_temp', lambda run: np.average(resultlib.get_memory_temperature_traces(run), axis=0), arch=arch_type, directory=directory)
        save_average(l3_runs, 'L3_temp', lambda run: resultlib.get_L3_temperature_trace(run), arch=arch_type, directory=directory)
        
        compare_runs(runs, 'core_power', 'Power (W)', lambda run: np.average(resultlib.get_core_power_traces(run), axis=0), arch=arch_type, directory=directory)
        compare_runs(runs, 'core_temps', 'Temperature (°C)', lambda run: np.average(resultlib.get_core_temperature_traces(run), axis=0), arch=arch_type, ylim=temps_lim, directory=directory)

        compare_runs(runs, 'mem_power', 'Power (W)', lambda run: np.average(resultlib.get_memory_power_traces(run), axis=0), arch=arch_type, directory=directory)
        compare_runs(runs, 'mem_temps', 'Temperature (°C)', lambda run: np.average(resultlib.get_memory_temperature_traces(run), axis=0), arch=arch_type, ylim=temps_lim, directory=directory)
        
        compare_runs(l3_runs, 'L3_power', 'Power (W)', lambda run: resultlib.get_L3_power_trace(run), arch=arch_type, directory=directory)
        compare_runs(l3_runs, 'L3_temps', 'Temperature (°C)', lambda run: resultlib.get_L3_temperature_trace(run), arch=arch_type, ylim=temps_lim, directory=directory)
        


if __name__ == '__main__':
    main('runs-2022-06-22_09.56')
    # temps_lim = (45,75)
    # runs = list(resultlib.get_runs())
    # runs = runs[-3:]
    # print('\n'.join(runs))
    # print_average(runs, 'core average', lambda run: np.average(resultlib.get_core_temperature_traces(run), axis=0))
    # print_average(runs, 'mem average', lambda run: np.average(resultlib.get_memory_temperature_traces(run), axis=0))

    # compare_runs(runs, 'core_power', 'Power (W)', lambda run: np.average(resultlib.get_core_power_traces(run), axis=0))
    # compare_runs(runs, 'core_temps', 'Temperature (C)', lambda run: np.average(resultlib.get_core_temperature_traces(run), axis=0), ylim=temps_lim)

    # compare_runs(runs, 'mem_power', 'Power (W)', lambda run: np.average(resultlib.get_memory_power_traces(run), axis=0))
    # compare_runs(runs, 'mem_temps', 'Temperature (C)', lambda run: np.average(resultlib.get_memory_temperature_traces(run), axis=0), ylim=temps_lim)
    
    # runs = runs [:-1]
    # compare_runs(runs, 'L3_power', 'Power (W)', lambda run: resultlib.get_L3_power_trace(run))
    # compare_runs(runs, 'L3_temps', 'Temperature (C)', lambda run: resultlib.get_L3_temperature_trace(run), ylim=temps_lim)
    # print_average(runs, 'L3 average', lambda run: resultlib.get_L3_temperature_trace(run))
    # for run in sorted(resultlib.get_runs())[::-1]:
    #     create_plots(run) 