from core.pipeline_fast import run_pipeline
from core.cache import set_cache


def run_full_analysis(job_id, df):
    result = run_pipeline(df)
    set_cache(job_id, result)