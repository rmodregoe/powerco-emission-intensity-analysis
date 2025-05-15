import logging
from scipy.spatial import cKDTree
import pandas as pd
import scr.config as config
logger = logging.getLogger(__name__)

class SpatialMatcher:
    @staticmethod
    def match_locations(df1: pd.DataFrame, df2: pd.DataFrame,
              tol: float = config.DISTANCE_THRESHOLD_DEG) -> pd.DataFrame:
        coords_df1 = df1[["Lat", "Long"]].to_numpy()
        coords_df2 = df2[["Lat", "Long"]].to_numpy()
        tree = cKDTree(coords_df2) #Build the tree with the largest dataset
        dists, idxs = tree.query(coords_df1, k=1, distance_upper_bound=tol) 
        mask = dists < tol
        logger.info("Matched %d of %d points under %.3f°",
                    mask.sum(), len(mask), tol)
        df1_matched = df1[mask].copy()
        df1_matched["df2_idx"] = idxs[mask]
        df1_matched = df1_matched.merge(df2[["Name", "Emissions (tCO2e)"]].assign(df2_idx=df2.index), on="df2_idx", how="left", suffixes = ("_df1", "_df2"))
        return df1_matched
