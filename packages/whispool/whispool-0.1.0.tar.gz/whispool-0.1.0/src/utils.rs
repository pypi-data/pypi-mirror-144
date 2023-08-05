pub fn id_in_ids(id_: usize, ids: &Vec<usize>) -> bool{
    /*
    Check if this is the piece is in the ids id list,
    using binary search

    ids should be sorted ascendingly
    */
    let id_len = ids.len();
    if id_len == 0{
        return false;
    } else if id_len == 1{
        return id_ == ids[0];
    } else {
        let mut start: usize = 0;
        let mut end: usize = id_len - 1;
        for _i in 0.. {
            let mid: usize = (start + end) / 2;

            if start > end {
                return false;
            } else if start == end {
                return id_ == ids[start];
            }
            let pick = ids[mid];
            if id_ == pick {
                return true;
            } else if id_ < pick {
                // left side
                end = (mid).max(1)-1;
            } else {
                // right side
                start = mid + 1;
            }
            
        }
        false
    }
}
