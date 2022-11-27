import argparse
import datetime

FROM_TO_TIME_DELIMITER = ' --> '

def create_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
                    prog = 'A python script to move subtitle timing')
    parser.add_argument('--source_file', type=str, required=True)
    parser.add_argument('--target_file', type=str, required=True)
    parser.add_argument('--time_shift_seconds', type=float)
    
    return parser


def _convert_one_time_point(time_str: str, time_shift_seconds: str) -> str:
    """Convert one time stamp.

    The original is something like 00:00:06,500, we need to output
    the same time with a shift.
    
    the format is therefore: hh:mm:ss,MMM where MMM is milliseconds (1/1000s), 
    all leading digits are preserved, e.g. 0 is "000"
    """
    
    format_str = "%H:%M:%S,%f"
    
    # we add "000" to be able to interprete milliseconds as microseconds
    date_object = datetime.datetime.strptime(time_str + "000", format_str)
    
    seconds_from_zero = (
        3600 * date_object.hour + 
        60 * date_object.minute + 
        date_object.second + 
        date_object.microsecond / 1_000_000
    )
    
    if seconds_from_zero + time_shift_seconds < 0:
        time_shift_seconds = -seconds_from_zero
    
    date_object = date_object + datetime.timedelta(seconds=time_shift_seconds)
        
    out_with_milliseconds = date_object.strftime(format_str)    
    return out_with_milliseconds[0:-3]
    

def _convert_time_line(time_line: str, time_shift_seconds: float) -> str:
    """Convert a time frame line to the one with shifted time
    
    example: the original one could be something like: 00:00:06,500 --> 00:00:10,208
    """
    parts = time_line.split(FROM_TO_TIME_DELIMITER)
    assert len(parts) == 2
    shifted_parts = [ _convert_one_time_point(part, time_shift_seconds) for part in parts]
    return FROM_TO_TIME_DELIMITER.join(shifted_parts)
    
def move_subtitles_time(source_file: str, target_file: str, time_shift_seconds: float):
    with open(source_file) as file:
        lines = [line.strip() for line in file]
        
    out_lines = []
    for line in lines:
        if FROM_TO_TIME_DELIMITER in line:
            out_lines.append(_convert_time_line(line, time_shift_seconds))
        else:
            out_lines.append(line)
    
    with open(target_file, "w") as file:
        for line in out_lines:
            print(line, file=file)