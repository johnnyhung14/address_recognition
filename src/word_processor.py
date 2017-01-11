import csv
import jieba


def cut_words():
    jieba.load_userdict("D:\\住宅小区经纬度数据\\dic")
    result = []
    with open("D:\\住宅小区经纬度数据\\result.csv", encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                address = row[2]
                seg_list = list(jieba.cut(address, cut_all=False))
                print([address, seg_list])
                words = '|'.join(seg_list)
                result.append([row[0].strip(), row[1], address, words])
            except Exception:
                pass

    with open("D:\\住宅小区经纬度数据\\结果.csv", encoding='utf-8', mode='xt', newline='') as file:
        writer = csv.writer(file)
        for row in result:
            writer.writerow(row)


cut_words()
