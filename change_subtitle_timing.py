import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__)))

from subtitles_timing_moving.subtitles_timing_moving import create_argument_parser, move_subtitles_time

if __name__ == "__main__":    
    parser = create_argument_parser()    
    args = parser.parse_args()    
    move_subtitles_time(args.source_file, args.target_file, args.time_shift_seconds)