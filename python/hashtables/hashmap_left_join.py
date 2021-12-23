from hashtables.hashtable import Hashtable

def hashmap_left_join(hashmap1, hashmap2):
    joined_tables = []
    for bucket in hashmap1.buckets:
        if bucket:
            is_current = bucket.head
            while is_current:
                is_current_key = is_current.value[0]
                is_current_value = is_current.value[1]
                group_pairs = [is_current_key, is_current_value]
                if hashmap2.contains(is_current_key):
                    group_pairs.append(hashmap2.get(is_current_key))
                else:
                    group_pairs.append(None)
                joined_tables.append(group_pairs)
                is_current = is_current.next

    return joined_tables
