(() => {
  'use strict';

  const LANGS = {
    ja: ['ja', '日本語', 'JP', '🇯🇵'],
    en: ['en', 'English', 'EN', '🇺🇸'],
    zh: ['zh-CN', '简体中文', '中文', '🇨🇳'],
    vi: ['vi', 'Tiếng Việt', 'VI', '🇻🇳'],
    ko: ['ko', '한국어', 'KO', '🇰🇷'],
    fil: ['fil', 'Filipino', 'FIL', '🇵🇭']
  };
  const CODES = ['en', 'zh', 'vi', 'ko', 'fil'];
  const R = [
    ['LOVELIER | 削らないことから始まる、自然な美しさ。','LOVELIER | Natural beauty begins with preserving your teeth.','LOVELIER｜从保留天然牙开始的自然之美。','LOVELIER | Vẻ đẹp tự nhiên bắt đầu từ việc bảo tồn răng thật.','LOVELIER | 자연치를 지키는 것에서 시작되는 자연스러운 아름다움.','LOVELIER | Nagsisimula ang likas na ganda sa pag-iingat ng natural na ngipin.'],
    ['本文へ移動','Skip to content','跳至正文','Chuyển đến nội dung','본문으로 이동','Lumaktaw sa nilalaman'],
    ['ラブリエとは','About LOVELIER','关于 LOVELIER','Về LOVELIER','LOVELIER 소개','Tungkol sa LOVELIER'],
    ['症例','Cases','案例','Ca điều trị','증례','Mga kaso'],
    ['特徴','Features','特点','Đặc điểm','특징','Mga tampok'],
    ['原先生','Dr. Hara','原医生','Bác sĩ Hara','하라 원장','Dr. Hara'],
    ['料金','Pricing','价格','Chi phí','비용','Presyo'],
    ['医院','Clinics','诊所','Phòng khám','병원','Mga klinika'],
    ['無料カウンセリング','Free consultation','免费咨询','Tư vấn miễn phí','무료 상담','Libreng konsultasyon'],
    ['メニューを開く','Open menu','打开菜单','Mở menu','메뉴 열기','Buksan ang menu'],
    ['メニューを閉じる','Close menu','关闭菜单','Đóng menu','메뉴 닫기','Isara ang menu'],
    ['削るセラミックの時代は終わりました。','The era of aggressively reducing teeth for veneers is over.','大量磨牙制作贴面的时代已经结束。','Thời đại mài nhiều mô răng để làm veneer đã kết thúc.','치아를 많이 삭제하는 세라믹 치료의 시대는 끝났습니다.','Tapos na ang panahon ng labis na pagbabawas ng ngipin para sa veneers.'],
    ['歯を削らない。','Preserve your natural teeth.','尽可能保留天然牙。','Ưu tiên bảo tồn răng thật.','자연치를 최대한 보존합니다.','Pangalagaan ang natural na ngipin.'],
    ['笑顔は、もっと','Let your smile feel','让笑容更加','Để nụ cười','미소는 더욱','Ang ngiti mo ay maaaring maging'],
    ['自然になれる。','more naturally yours.','自然、属于你。','tự nhiên hơn, đúng với bạn hơn.','자연스러워질 수 있습니다.','mas natural at mas ikaw.'],
    ['最薄0.04mmからのジルコニアベニア','Ultra-thin zirconia veneers from 0.04 mm','薄至0.04毫米的氧化锆贴面','Veneer zirconia siêu mỏng từ 0,04 mm','최박 0.04mm부터 설계하는 지르코니아 베니어','Ultra-thin zirconia veneers mula 0.04 mm'],
    ['症例で見る、ラブリエの変化','See the LOVELIER transformation','通过案例了解 LOVELIER 的变化','Xem sự thay đổi với LOVELIER','증례로 보는 LOVELIER의 변화','Tingnan ang pagbabago sa LOVELIER'],
    ['ノアさん・上下20本 ↗','Noa · 20 upper and lower veneers ↗','Noa · 上下共20颗 ↗','Noa · 20 răng hàm trên và dưới ↗','Noa · 상하 20개 ↗','Noa · 20 upper at lower veneers ↗'],
    ['歯の色や形だけでなく、唇、横顔、笑ったときの見え方まで。','Beyond tooth color and shape—we consider the lips, profile and how the smile appears.','不仅关注牙齿的颜色和形状，也关注嘴唇、侧脸以及微笑时的整体效果。','Không chỉ màu sắc và hình dáng răng, chúng tôi còn xem xét môi, góc nghiêng và nụ cười.','치아의 색과 형태뿐 아니라 입술, 옆모습, 웃을 때의 인상까지 확인합니다.','Hindi lang kulay at hugis ng ngipin—isinasaalang-alang din ang labi, profile at buong ngiti.'],
    ['お顔全体との調和を見ながら、一人ひとりの口元を設計します。','Each smile is designed in harmony with the entire face.','结合面部整体协调，为每位患者设计笑容。','Thiết kế nụ cười riêng cho từng người, hài hòa với toàn bộ khuôn mặt.','얼굴 전체와의 조화를 보며 한 분 한 분의 미소를 디자인합니다.','Idinidisenyo ang bawat ngiti upang bumagay sa buong mukha.'],
    ['顔貌まで見た','Designed with the whole face in mind','兼顾面部整体','Thiết kế dựa trên toàn bộ khuôn mặt','얼굴 전체를 고려한','Disenyong isinasaalang-alang ang buong mukha'],
    ['ジルコニアベニア症例','Zirconia veneer case','氧化锆贴面案例','Ca veneer zirconia','지르코니아 베니어 증례','Zirconia veneer case'],
    ['上下20本・全顔モニター','20 upper and lower veneers · full-face monitor','上下共20颗 · 全脸模特方案','20 răng hàm trên và dưới · gói hình ảnh toàn mặt','상하 20개 · 전안면 모니터','20 upper at lower veneers · full-face monitor'],
    ['自然な笑顔と、顔全体との調和へ。','A natural smile, in harmony with the whole face.','打造自然笑容，与面部整体和谐。','Nụ cười tự nhiên, hài hòa với toàn bộ khuôn mặt.','자연스러운 미소와 얼굴 전체의 조화.','Isang natural na ngiti na kaayon ng buong mukha.'],
    ['無料カウンセリングを予約する','Book a free consultation','预约免费咨询','Đặt lịch tư vấn miễn phí','무료 상담 예약','Mag-book ng libreng konsultasyon'],
    ['症例を見る','View cases','查看案例','Xem ca điều trị','증례 보기','Tingnan ang mga kaso'],
    ['適応には個人差があります。診査・カウンセリング後に治療可否をご案内します。','Suitability varies. Treatment eligibility is confirmed after examination and consultation.','适应情况因人而异。检查和咨询后将告知是否适合治疗。','Khả năng phù hợp tùy từng người. Chúng tôi sẽ xác nhận sau khi thăm khám và tư vấn.','적응 여부는 개인차가 있으며 진단과 상담 후 안내드립니다.','Nag-iiba ang pagiging angkop sa bawat tao. Kukumpirmahin ito pagkatapos ng pagsusuri at konsultasyon.'],
    ['削らないことを軸に','Preservation-first care','以保留天然牙为核心','Điều trị ưu tiên bảo tồn','치아 보존을 중심으로','Pangangalagang inuuna ang pagpreserba'],
    ['天然歯を残すことから治療計画を考えます','Treatment planning begins with preserving natural teeth','治疗计划从保留天然牙开始','Lập kế hoạch điều trị bắt đầu từ bảo tồn răng thật','자연치를 보존하는 것부터 치료 계획을 세웁니다','Nagsisimula ang plano sa pagpreserba ng natural na ngipin'],
    ['日本一の症例数を誇る','Japan’s leading LOVELIER case volume','LOVELIER案例数量日本领先','Số ca LOVELIER hàng đầu Nhật Bản','일본 최고 수준의 LOVELIER 증례 수','Nangunguna sa Japan sa dami ng LOVELIER cases'],
    ['医療法人清翔会','SEISHOKAI Medical Corporation','医疗法人清翔会','Tập đoàn Y tế SEISHOKAI','의료법인 세이쇼카이','SEISHOKAI Medical Corporation'],
    ['ラブリエ症例数／医療法人清翔会グループ提供情報に基づく','LOVELIER case volume / based on information provided by SEISHOKAI','LOVELIER案例数量／依据清翔会集团提供的信息','Số ca LOVELIER / dựa trên thông tin do SEISHOKAI cung cấp','LOVELIER 증례 수 / 세이쇼카이 제공 정보 기준','Dami ng LOVELIER cases / batay sa impormasyong ibinigay ng SEISHOKAI'],
    ['1本あたり最安','Lowest price per veneer','每颗最低','Giá thấp nhất mỗi veneer','1개당 최저가','Pinakamababang presyo bawat veneer'],
    ['デンタルローン 月々約17,400円〜','Dental loan from approx. JPY 17,400/month','牙科贷款每月约17,400日元起','Vay nha khoa từ khoảng 17.400 JPY/tháng','덴탈론 월 약 17,400엔부터','Dental loan mula humigit-kumulang JPY 17,400/buwan'],
    ['ノアさんの','Noa’s','Noa 的','Nụ cười của Noa','Noa의','Ang kay Noa'],
    ['自然な表情を、そのまま。','natural expression, preserved.','自然神态，真实保留。','biểu cảm tự nhiên, được giữ trọn.','자연스러운 표정을 그대로.','natural na ekspresyon, pinananatili.'],
    ['口元だけを切り取らず、表情や横顔まで含めて見ること。ラブリエが大切にするのは、その人らしい笑顔のバランスです。','We look beyond the mouth to the expression and profile. LOVELIER values a smile that feels true to the individual.','不只看口唇，也观察表情和侧脸。LOVELIER重视属于每个人自己的笑容平衡。','Chúng tôi nhìn cả biểu cảm và góc nghiêng, không chỉ riêng vùng miệng. LOVELIER coi trọng nụ cười đúng với mỗi người.','입만 보지 않고 표정과 옆모습까지 살핍니다. LOVELIER는 그 사람다운 미소의 균형을 중요하게 생각합니다.','Tinitingnan namin ang ekspresyon at profile, hindi lamang ang bibig. Mahalaga sa LOVELIER ang ngiting tunay na iyo.'],
    ['掲載写真は実在するノアさんの撮影素材です。治療内容・期間・費用・結果には個人差があります。','Photos feature the real Noa. Treatment, duration, cost and results vary by individual.','照片为Noa本人拍摄素材。治疗内容、疗程、费用和结果因人而异。','Ảnh chụp là của Noa thật. Nội dung, thời gian, chi phí và kết quả điều trị khác nhau tùy người.','게재 사진은 실제 Noa의 촬영 자료입니다. 치료 내용·기간·비용·결과에는 개인차가 있습니다.','Ang mga larawan ay kay Noa mismo. Nag-iiba ang paggamot, tagal, gastos at resulta sa bawat tao.'],
    ['ノアさんの変化を、','Noa’s transformation,','Noa 的变化，','Sự thay đổi của Noa,','Noa의 변화,','Ang pagbabago ni Noa,'],
    ['顔貌から口腔内まで。','from facial profile to the mouth.','从面容到口腔内部。','từ khuôn mặt đến trong miệng.','얼굴부터 구강 내까지.','mula sa mukha hanggang sa loob ng bibig.'],
    ['お悩み','Concern','主要问题','Vấn đề','고민','Alalahanin'],
    ['歯のガタつき・歯を白くしたい','Uneven teeth · desire for a brighter smile','牙齿不齐 · 希望改善色泽','Răng không đều · muốn răng sáng hơn','치아 배열 불규칙 · 미백 희망','Hindi pantay na ngipin · nais ng mas maliwanag na ngiti'],
    ['治療内容','Treatment','治疗内容','Điều trị','치료 내용','Paggamot'],
    ['上下20本','20 upper and lower veneers','上下共20颗','20 răng hàm trên và dưới','상하 20개','20 upper at lower veneers'],
    ['費用','Cost','费用','Chi phí','비용','Gastos'],
    ['1,738,000円（税込）','JPY 1,738,000 (tax included)','1,738,000日元（含税）','1.738.000 JPY (đã gồm thuế)','1,738,000엔(세금 포함)','JPY 1,738,000 (kasama ang buwis)'],
    ['全顔モニター価格','Full-face monitor price','全脸模特方案价格','Giá gói hình ảnh toàn mặt','전안면 모니터 가격','Full-face monitor price'],
    ['治療前','Before treatment','治疗前','Trước điều trị','치료 전','Bago ang paggamot'],
    ['治療後','After treatment','治疗后','Sau điều trị','치료 후','Pagkatapos ng paggamot'],
    ['歯だけではなく、','Beyond the teeth,','不仅是牙齿，','Không chỉ riêng răng,','치아만이 아니라,','Higit pa sa ngipin,'],
    ['笑顔全体に調和するデザインへ。','a design in harmony with the entire smile.','打造与整体笑容协调的设计。','thiết kế hài hòa với toàn bộ nụ cười.','미소 전체와 조화되는 디자인.','isang disenyong kaayon ng buong ngiti.'],
    ['顔貌・口元・横顔を多角的に確認し、笑顔全体との調和を見ながらデザインします。','We assess the face, mouth and profile from multiple angles to design for harmony with the whole smile.','从多个角度确认面容、口唇和侧脸，并结合整体笑容进行设计。','Đánh giá khuôn mặt, vùng miệng và góc nghiêng từ nhiều góc độ để thiết kế hài hòa.','얼굴·입·옆모습을 다각도로 확인하여 미소 전체와 조화되도록 디자인합니다.','Sinusuri ang mukha, bibig at profile mula sa iba’t ibang anggulo upang maging balanse ang buong ngiti.'],
    ['天然歯を残しながら、','Preserve natural teeth,','保留天然牙，','Bảo tồn răng thật,','자연치를 보존하면서,','Pinananatili ang natural na ngipin,'],
    ['色と形を整える。','refine color and shape.','改善颜色与形状。','điều chỉnh màu sắc và hình dáng.','색과 형태를 다듬습니다.','inaayos ang kulay at hugis.'],
    ['「人工ダイヤモンド」','“Artificial diamond”','“人造钻石”','“Kim cương nhân tạo”','“인공 다이아몬드”','“Artipisyal na diyamante”'],
    ['とも称されるジルコニア。','—a name often used for zirconia.','——氧化锆常被如此称呼。','—cách zirconia thường được gọi.','라고도 불리는 지르코니아.','—tawag na madalas gamitin para sa zirconia.'],
    ['その強さを、最薄0.04mmからの繊細さへ。','Strength refined into delicacy from just 0.04 mm.','将其强度化为薄至0.04毫米的精细设计。','Biến độ bền thành sự tinh tế từ độ mỏng 0,04 mm.','그 강도를 최박 0.04mm부터의 섬세함으로.','Lakas na hinubog sa nipis mula 0.04 mm.'],
    ['※歯科用ジルコニアは、ダイヤモンドとは異なるセラミック材料です。','* Dental zirconia is a ceramic material and is not diamond.','※牙科氧化锆是与钻石不同的陶瓷材料。','* Zirconia nha khoa là vật liệu gốm, không phải kim cương.','※치과용 지르코니아는 다이아몬드와 다른 세라믹 재료입니다.','* Ang dental zirconia ay ceramic material at hindi diyamante.'],
    ['薄さは、','Thinness,','薄，','Độ mỏng,','얇음은,','Ang nipis,'],
    ['自然さのために。','for a natural result.','是为了自然。','vì vẻ tự nhiên.','자연스러움을 위해.','para sa natural na resulta.'],
    ['口元のお悩み、','Your smile concerns—','关于口唇的烦恼，','Điều bạn băn khoăn về nụ cười—','입가 고민,','Mga alalahanin sa ngiti—'],
    ['どれに近いですか。','which feels closest to yours?','哪一项最接近您？','điều nào gần với bạn nhất?','어느 쪽에 가깝나요?','alin ang pinakamalapit sa iyo?'],
    ['前歯のすき間','Gaps between front teeth','前牙缝隙','Khe giữa răng cửa','앞니 사이 틈','Agwat sa harapang ngipin'],
    ['歯間の黒いすき間','Black triangles','牙缝黑三角','Tam giác đen kẽ răng','블랙 트라이앵글','Black triangles'],
    ['歯の黄ばみ・色味','Yellowing and shade','牙齿发黄与色泽','Răng ố vàng và màu sắc','치아 황변·색조','Paninilaw at kulay'],
    ['歯の白斑・表面','White spots and surface texture','白斑与牙面','Đốm trắng và bề mặt răng','백반·표면','White spots at ibabaw'],
    ['関連症例を見る →','View related cases →','查看相关案例 →','Xem ca liên quan →','관련 증례 보기 →','Tingnan ang kaugnay na kaso →'],
    ['残すこと。薄くすること。','Preserve. Keep it thin.','保留天然牙，轻薄设计。','Bảo tồn. Giữ thật mỏng.','보존하고, 얇게.','Magpreserba. Panatilihing manipis.'],
    ['その人らしく','Design for','为每个人','Thiết kế','그 사람답게','Disenyo para sa'],
    ['設計すること。','the individual.','量身设计。','cho riêng bạn.','디자인합니다.','bawat tao.'],
    ['歯を削らないことを基本とする','Preservation-first by principle','以尽量不磨牙为基本原则','Nguyên tắc ưu tiên không mài răng','치아 삭제를 하지 않는 것을 기본으로','Pangunahing prinsipyo ang hindi pagtabas ng ngipin'],
    ['最薄0.04mmからの極薄加工','Ultra-thin fabrication from 0.04 mm','薄至0.04毫米的超薄加工','Chế tác siêu mỏng từ 0,04 mm','최박 0.04mm부터의 초박형 가공','Ultra-thin na paggawa mula 0.04 mm'],
    ['高強度ジルコニア','High-strength zirconia','高强度氧化锆','Zirconia độ bền cao','고강도 지르코니아','High-strength zirconia'],
    ['顔貌に合わせたオーダーデザイン','Custom design for facial harmony','配合面容的定制设计','Thiết kế riêng hài hòa khuôn mặt','얼굴에 맞춘 맞춤 디자인','Custom design para sa buong mukha'],
    ['症例を、悩み別に見る。','Browse cases by concern.','按问题查看案例。','Xem ca theo vấn đề.','고민별 증례 보기.','Tingnan ang cases ayon sa alalahanin.'],
    ['すきっ歯・歯の形','Gaps · tooth shape','牙缝 · 牙齿形状','Khe răng · hình dáng răng','치아 사이 틈 · 형태','Agwat · hugis ng ngipin'],
    ['すきっ歯・色味','Gaps · shade','牙缝 · 色泽','Khe răng · màu sắc','치아 사이 틈 · 색조','Agwat · kulay'],
    ['歯のガタつき','Uneven teeth','牙齿不齐','Răng không đều','치아 배열 불규칙','Hindi pantay na ngipin'],
    ['歯の色味','Tooth shade','牙齿色泽','Màu răng','치아 색조','Kulay ng ngipin'],
    ['正中離開','Midline gap','正中牙缝','Khe đường giữa','정중 이개','Midline gap'],
    ['すきっ歯・上下の調和','Gaps · upper/lower harmony','牙缝 · 上下协调','Khe răng · hài hòa hai hàm','치아 사이 틈 · 상하 조화','Agwat · balanse ng upper/lower'],
    ['症例情報・リスク','Case details and risks','案例信息与风险','Thông tin ca và rủi ro','증례 정보·위험','Detalye at panganib'],
    ['症例をもっと見る','View more cases','查看更多案例','Xem thêm ca','증례 더 보기','Tingnan pa ang cases'],
    ['素材の違いを、','Understand materials,','了解材料差异，','Hiểu sự khác nhau của vật liệu,','소재의 차이를,','Unawain ang materyales,'],
    ['治療選択の違いへ。','to understand treatment choices.','从而理解治疗选择。','để lựa chọn điều trị phù hợp.','치료 선택의 차이로.','upang piliin ang paggamot.'],
    ['比較項目','Comparison','比较项目','Hạng mục','비교 항목','Paghahambing'],
    ['セラミックベニア','Ceramic veneer','陶瓷贴面','Veneer sứ','세라믹 베니어','Ceramic veneer'],
    ['ジルコニアベニア','Zirconia veneer','氧化锆贴面','Veneer zirconia','지르코니아 베니어','Zirconia veneer'],
    ['素材','Material','材料','Vật liệu','소재','Materyal'],
    ['薄さ','Thickness','厚度','Độ dày','두께','Kapal'],
    ['色の遮蔽性','Color masking','遮色性','Khả năng che màu','색상 차폐성','Color masking'],
    ['自然感','Natural appearance','自然感','Vẻ tự nhiên','자연스러움','Natural na itsura'],
    ['歯の切削','Tooth reduction','牙体磨削','Mài răng','치아 삭제','Pagbawas ng ngipin'],
    ['強度','Strength','强度','Độ bền','강도','Lakas'],
    ['適応条件','Suitability','适应条件','Điều kiện chỉ định','적응 조건','Pagiging angkop'],
    ['適応本数','Number of teeth','适用颗数','Số răng','적응 개수','Bilang ng ngipin'],
    ['価格傾向','Price tendency','价格趋势','Xu hướng chi phí','가격 경향','Price range'],
    ['適応症例の場合','For suitable cases','适用案例','Với ca phù hợp','적응 증례의 경우','Para sa angkop na kaso'],
    ['通院','Visits','到院','Lần đến khám','내원','Pagbisita'],
    ['回。','visits.','次。','lần.','회.','beses.'],
    ['相談・精密スキャンから、ラブリエセットまで。','From consultation and precision scan to final LOVELIER placement.','从咨询和精密扫描到LOVELIER安装。','Từ tư vấn, quét chính xác đến gắn LOVELIER.','상담·정밀 스캔부터 LOVELIER 세팅까지.','Mula konsultasyon at precision scan hanggang LOVELIER placement.'],
    ['デザイン確認はLINEまたはメールで行えます。','Design approval is available via LINE or email.','可通过LINE或电子邮件确认设计。','Có thể duyệt thiết kế qua LINE hoặc email.','디자인 확인은 LINE 또는 이메일로 가능합니다.','Maaaring aprubahan ang design sa LINE o email.'],
    ['来院1回目','Visit 1','第1次到院','Lần khám 1','1회차 내원','Unang pagbisita'],
    ['来院1回目・同日','Visit 1 · same day','第1次到院 · 当天','Lần khám 1 · cùng ngày','1회차 내원 · 당일','Unang pagbisita · parehong araw'],
    ['精密スキャン・色調選択','Precision scan and shade selection','精密扫描与色调选择','Quét chính xác và chọn màu','정밀 스캔·색조 선택','Precision scan at pagpili ng shade'],
    ['オンライン','Online','线上','Trực tuyến','온라인','Online'],
    ['デザイン確認','Design approval','设计确认','Duyệt thiết kế','디자인 확인','Pag-apruba ng design'],
    ['来院2回目','Visit 2','第2次到院','Lần khám 2','2회차 내원','Ikalawang pagbisita'],
    ['ラブリエセット','LOVELIER placement','安装LOVELIER','Gắn LOVELIER','LOVELIER 세팅','LOVELIER placement'],
    ['アフターケア','Aftercare','后续护理','Chăm sóc sau điều trị','사후 관리','Aftercare'],
    ['定期検診','Regular checkups','定期检查','Tái khám định kỳ','정기 검진','Regular checkup'],
    ['本数ごとの料金を、','Pricing by number,','按颗数查看价格，','Chi phí theo số răng,','개수별 요금을,','Presyo ayon sa bilang,'],
    ['ひと目で。','at a glance.','一目了然。','xem nhanh.','한눈에.','sa isang tingin.'],
    ['デンタルローン 120回払い','Dental loan · 120 payments','牙科贷款 · 120期','Vay nha khoa · 120 kỳ','덴탈론 · 120회','Dental loan · 120 hulog'],
    ['大きな金額が、月々のお支払い目安です','See the estimated monthly payment for each option','将总价转换为每月付款参考','Xem mức thanh toán hàng tháng dự kiến','월 납입 예상액을 확인하세요','Tingnan ang tinatayang buwanang bayad'],
    ['想定年率3.7%で算出','Calculated at an assumed annual rate of 3.7%','按假定年利率3.7%计算','Tính theo lãi suất giả định 3,7%/năm','가정 연이율 3.7%로 계산','Kinalkula sa 3.7% na taunang interes'],
    ['本数','Number','颗数','Số răng','개수','Bilang'],
    ['定価','Standard price','标准价','Giá tiêu chuẩn','정가','Regular price'],
    ['鼻下モニター','Mouth-area monitor','口唇区域模特方案','Gói hình vùng miệng','비순부 모니터','Mouth-area monitor'],
    ['顔モニター','Full-face monitor','全脸模特方案','Gói hình toàn mặt','전안면 모니터','Full-face monitor'],
    ['おすすめ','Recommended','推荐','Đề xuất','추천','Recommended'],
    ['月々のお支払い','Monthly payment','每月付款','Thanh toán hàng tháng','월 납입액','Buwanang bayad'],
    ['1本あたり','Per veneer','每颗','Mỗi veneer','1개당','Bawat veneer'],
    ['モニター条件','Monitor conditions','模特方案条件','Điều kiện hình ảnh','모니터 조건','Monitor conditions'],
    ['料金について','About pricing','关于价格','Về chi phí','요금 안내','Tungkol sa presyo'],
    ['分割払い','Installments','分期付款','Trả góp','분할 납부','Installment'],
    ['料金と適応本数を相談する','Discuss pricing and number of veneers','咨询价格和适用颗数','Tư vấn chi phí và số răng','요금과 적응 개수 상담','Talakayin ang presyo at bilang ng veneers'],
    ['治療前に、','Before treatment,','治疗前，','Trước điều trị,','치료 전에,','Bago ang paggamot,'],
    ['知っていただきたいこと。','what you should know.','需要了解的事项。','những điều cần biết.','알아두셔야 할 점.','mga dapat mong malaman.'],
    ['保証適用条件','Warranty conditions','保修适用条件','Điều kiện bảo hành','보증 적용 조건','Warranty conditions'],
    ['保証対象外','Not covered','不在保修范围','Không được bảo hành','보증 제외','Hindi sakop'],
    ['ラブリエ症例数','LOVELIER case volume','LOVELIER案例数量','Số ca LOVELIER','LOVELIER 증례 수','Dami ng LOVELIER cases'],
    ['日本一','No. 1 in Japan','日本第一','Số 1 Nhật Bản','일본 1위','No. 1 sa Japan'],
    ['副理事長','Vice Chairman','副理事长','Phó Chủ tịch','부이사장','Vice Chairman'],
    ['矯正医として、たどり着いた境地。','A philosophy shaped by years in orthodontics.','这是多年正畸实践后形成的治疗理念。','Triết lý được đúc kết từ nhiều năm điều trị chỉnh nha.','교정 진료 경험 끝에 도달한 치료 철학입니다.','Isang pilosopiyang hinubog ng maraming taon sa orthodontics.'],
    ['医院都合ではなく、患者様の想いをカタチに。','Care shaped around your vision—not the clinic’s convenience.','不以诊所方便为先，而将患者的期望化为现实。','Hiện thực hóa mong muốn của bệnh nhân, không đặt sự thuận tiện của phòng khám lên trước.','병원의 편의가 아닌, 환자분의 바람을 형태로 만듭니다.','Hinuhubog namin ang nais ng pasyente—hindi ang kaginhawaan ng klinika.'],
    ['経歴','Career','履历','Kinh nghiệm','경력','Karera'],
    ['所属・資格','Affiliations and qualifications','所属与资质','Hiệp hội và chứng chỉ','소속·자격','Affiliations at qualifications'],
    ['お近くの医院で、','At a clinic near you,','在您附近的诊所，','Tại phòng khám gần bạn,','가까운 병원에서,','Sa klinika na malapit sa iyo,'],
    ['無料カウンセリング。','a free consultation.','免费咨询。','tư vấn miễn phí.','무료 상담.','libreng konsultasyon.'],
    ['医療法人清翔会グループの下記医院でラブリエをご相談いただけます。','LOVELIER consultations are available at the SEISHOKAI clinics below.','可在以下清翔会集团诊所咨询LOVELIER。','Có thể tư vấn LOVELIER tại các phòng khám SEISHOKAI dưới đây.','아래 세이쇼카이 병원에서 LOVELIER 상담이 가능합니다.','Available ang LOVELIER consultation sa mga SEISHOKAI clinic sa ibaba.'],
    ['予約する →','Book now →','立即预约 →','Đặt lịch →','예약하기 →','Mag-book →'],
    ['よくあるご質問。','Frequently asked questions.','常见问题。','Câu hỏi thường gặp.','자주 묻는 질문.','Mga madalas itanong.'],
    ['本当に歯を削らないのですか','Are the teeth really not reduced?','真的不磨牙吗？','Có thực sự không mài răng không?','정말 치아를 삭제하지 않나요?','Talagang hindi binabawasan ang ngipin?'],
    ['誰でも治療できますか','Is treatment suitable for everyone?','任何人都能接受治疗吗？','Ai cũng có thể điều trị không?','누구나 치료할 수 있나요?','Angkop ba ito sa lahat?'],
    ['ガタつきがあっても可能ですか','Can uneven teeth be treated?','牙齿不齐也可以吗？','Răng không đều có làm được không?','치열이 고르지 않아도 가능한가요?','Puwede ba kung hindi pantay ang ngipin?'],
    ['前歯が出て見えませんか','Will my front teeth look prominent?','前牙会显得突出吗？','Răng trước có trông nhô ra không?','앞니가 돌출되어 보이지 않나요?','Magmumukhang nakausli ba ang harapang ngipin?'],
    ['痛みはありますか','Will it hurt?','会疼吗？','Có đau không?','통증이 있나요?','Masakit ba?'],
    ['何本から治療できますか','What is the minimum number of veneers?','最少可以做几颗？','Có thể làm từ bao nhiêu răng?','몇 개부터 치료할 수 있나요?','Ilang veneer ang minimum?'],
    ['何回通院しますか','How many visits are required?','需要到院几次？','Cần đến khám bao nhiêu lần?','몇 번 내원하나요?','Ilang pagbisita ang kailangan?'],
    ['完成までどれくらいですか','How long until completion?','完成需要多久？','Mất bao lâu để hoàn tất?','완성까지 얼마나 걸리나요?','Gaano katagal bago matapos?'],
    ['色や形はどう決めますか','How are color and shape chosen?','如何决定颜色和形状？','Chọn màu và hình dáng như thế nào?','색과 형태는 어떻게 정하나요?','Paano pinipili ang kulay at hugis?'],
    ['装着後に色や形を変えられますか','Can color or shape be changed after placement?','安装后可以改变颜色或形状吗？','Có thể đổi màu hoặc hình dáng sau khi gắn không?','장착 후 색이나 형태를 바꿀 수 있나요?','Mababago ba ang kulay o hugis pagkatapos ikabit?'],
    ['外すことはできますか','Can veneers be removed?','可以取下吗？','Có thể tháo ra không?','제거할 수 있나요?','Maaari bang tanggalin?'],
    ['どのくらい長持ちしますか','How long do they last?','可以使用多久？','Dùng được bao lâu?','얼마나 오래 사용할 수 있나요?','Gaano katagal ito tumatagal?'],
    ['保証はありますか','Is there a warranty?','有保修吗？','Có bảo hành không?','보증이 있나요?','May warranty ba?'],
    ['削らずにできるか、','Could this be done without reducing your teeth?','能否不磨牙完成，','Có thể thực hiện mà không mài răng không,','삭제하지 않고 가능한지,','Posible ba nang hindi binabawasan ang ngipin,'],
    ['あなたの笑顔を見ながら。','Let us assess it with your smile in view.','让我们结合您的笑容进行判断。','hãy để chúng tôi đánh giá cùng nụ cười của bạn.','당신의 미소를 보며 확인합니다.','susuriin namin habang tinitingnan ang iyong ngiti.'],
    ['初回相談無料','First consultation free','首次咨询免费','Tư vấn lần đầu miễn phí','첫 상담 무료','Libreng unang konsultasyon'],
    ['各医院で受付','Available at each clinic','各诊所均可受理','Tiếp nhận tại mỗi phòng khám','각 병원에서 접수','Available sa bawat klinika'],
    ['オンライン予約','Online booking','在线预约','Đặt lịch trực tuyến','온라인 예약','Online booking'],
    ['各医院共通のオンライン予約画面へ進みます。','You will proceed to the shared online booking page for all clinics.','将进入各诊所共用的在线预约页面。','Bạn sẽ chuyển đến trang đặt lịch chung cho các phòng khám.','각 병원 공통 온라인 예약 화면으로 이동합니다.','Pupunta ka sa shared online booking page ng mga klinika.'],
    ['無料相談を予約する','Book a free consultation','预约免费咨询','Đặt lịch tư vấn miễn phí','무료 상담 예약','Mag-book ng libreng konsultasyon'],
    ['治療の適応・期間・費用・結果には個人差があります。診査のうえで詳しくご案内します。','Suitability, duration, cost and results vary. Details are provided after examination.','适应情况、疗程、费用和结果因人而异，检查后将详细说明。','Chỉ định, thời gian, chi phí và kết quả khác nhau tùy người. Chi tiết được giải thích sau khi khám.','적응·기간·비용·결과에는 개인차가 있으며 진단 후 자세히 안내드립니다.','Nag-iiba ang pagiging angkop, tagal, gastos at resulta. Ipaliwanag ang detalye pagkatapos ng pagsusuri.'],
    ['無料カウンセリングを予約','Book a free consultation','预约免费咨询','Đặt lịch tư vấn miễn phí','무료 상담 예약','Mag-book ng libreng konsultasyon']
  ];

  const clean = (value) => (value || '').replace(/\s+/g, ' ').trim();
  const rows = R.concat(window.LOVELIER_I18N_SUPPLEMENT || []);
  const dictionaries = Object.fromEntries(CODES.map((code, i) => [code, new Map(rows.map((row) => [clean(row[0]), row[i + 1]]))]));
  const sources = new WeakMap();
  const attributeSources = new WeakMap();

  function pattern(source, language) {
    let match = source.match(/^約\s*([\d,]+)円〜$/);
    if (match) {
      const amount = match[1];
      if (language === 'zh') return `约 ${amount} 日元起`;
      if (language === 'vi') return `Khoảng ${amount} JPY`;
      if (language === 'ko') return `약 ${amount}엔부터`;
      if (language === 'fil') return `Humigit-kumulang JPY ${amount}`;
      return `Approx. JPY ${amount}`;
    }
    match = source.match(/^([\d,]+)円$/);
    if (match) return language === 'zh' ? `${match[1]}日元` : language === 'ko' ? `${match[1]}엔` : `${match[1]} JPY`;
    match = source.match(/^(\d+)本$/);
    if (match) return language === 'zh' ? `${match[1]}颗` : language === 'vi' ? `${match[1]} răng` : language === 'ko' ? `${match[1]}개` : `${match[1]} veneers`;
    return source;
  }

  function t(source, language = document.documentElement.dataset.language || 'ja') {
    const value = clean(source);
    return language === 'ja' ? value : dictionaries[language]?.get(value) || pattern(value, language);
  }

  function capture() {
    const walker = document.createTreeWalker(document.documentElement, NodeFilter.SHOW_TEXT, {
      acceptNode(node) {
        return node.parentElement?.closest('script,style,[data-language-switcher]') || !clean(node.nodeValue)
          ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT;
      }
    });
    let node;
    while ((node = walker.nextNode())) sources.set(node, node.nodeValue);
    document.querySelectorAll('[alt],[aria-label],[title],[placeholder]').forEach((element) => {
      const values = {};
      ['alt','aria-label','title','placeholder'].forEach((name) => {
        if (element.hasAttribute(name)) values[name] = element.getAttribute(name);
      });
      attributeSources.set(element, values);
    });
  }

  function apply(language, options = {}) {
    if (!LANGS[language]) language = 'ja';
    const walker = document.createTreeWalker(document.documentElement, NodeFilter.SHOW_TEXT, {
      acceptNode: (node) => sources.has(node) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT
    });
    let node;
    while ((node = walker.nextNode())) {
      const original = sources.get(node);
      const leading = original.match(/^\s*/)?.[0] || '';
      const trailing = original.match(/\s*$/)?.[0] || '';
      node.nodeValue = `${leading}${t(original, language)}${trailing}`;
    }
    document.querySelectorAll('[alt],[aria-label],[title],[placeholder]').forEach((element) => {
      const original = attributeSources.get(element);
      if (!original) return;
      Object.entries(original).forEach(([name, value]) => element.setAttribute(name, t(value, language)));
    });
    document.documentElement.lang = LANGS[language][0];
    document.documentElement.dataset.language = language;
    document.querySelectorAll('[data-language]').forEach((button) => {
      const active = button.dataset.language === language;
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-pressed', String(active));
    });
    document.querySelectorAll('.comparison-grid > div').forEach((row) => {
      row.querySelector(':scope > p:nth-of-type(1)')?.setAttribute('data-label', t('セラミックベニア', language));
      row.querySelector(':scope > p:nth-of-type(2)')?.setAttribute('data-label', t('ジルコニアベニア', language));
    });
    document.title = t('LOVELIER | 削らないことから始まる、自然な美しさ。', language);
    if (options.persist !== false) {
      try { localStorage.setItem('lovelier-language', language); } catch (_) { /* Storage may be unavailable in local previews. */ }
      const url = new URL(location.href);
      language === 'ja' ? url.searchParams.delete('lang') : url.searchParams.set('lang', language);
      history.replaceState(null, '', `${url.pathname}${url.search}${url.hash}`);
    }
    window.dispatchEvent(new CustomEvent('lovelier:languagechange', { detail: { language } }));
  }

  function init() {
    capture();
    const requested = new URLSearchParams(location.search).get('lang');
    let saved = null;
    try { saved = localStorage.getItem('lovelier-language'); } catch (_) { /* Default to Japanese when storage is unavailable. */ }
    const initial = LANGS[requested] ? requested : LANGS[saved] ? saved : 'ja';
    document.querySelectorAll('[data-language]').forEach((button) => button.addEventListener('click', () => apply(button.dataset.language)));
    apply(initial, { persist: false });
  }

  window.LovelierI18n = { t, apply, languages: LANGS };
  document.readyState === 'loading' ? document.addEventListener('DOMContentLoaded', init, { once: true }) : init();
})();
