from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def buttonPaginator(page_button_range, paginator, page, paged_bars):
    page_button_range = page_button_range
    page_button_group = 1
    #print('paginator.num_pages: ', paginator.num_pages)

    page_button_number_of_groups = int(paginator.num_pages / page_button_range)
    remainder = paginator.num_pages % page_button_range
    if remainder > 0:
        page_button_number_of_groups = page_button_number_of_groups + 1

    #print('page_button_number_of_groups: ',page_button_number_of_groups)

    page_button_group = int (int(page) / page_button_range)
    remainder = int(page) % page_button_range
    if remainder > 0:
        page_button_group = page_button_group + 1       
    #print('page_button_group: ',page_button_group)
    
    leftIndex = ((page_button_group-1)*page_button_range)+1
    rightIndex = leftIndex + page_button_range
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
        leftIndex = rightIndex - page_button_range
    if leftIndex < 0:
        leftIndex = 1


    custom_range = paged_bars.paginator.page_range
    custom_range = range(leftIndex,rightIndex)
    #print('custom_range: ', custom_range)

    return custom_range
