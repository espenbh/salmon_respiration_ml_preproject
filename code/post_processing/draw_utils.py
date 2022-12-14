import cv2
import torchvision.transforms as T
import numpy as np
import torch
import torchvision

# Draw bounding boxes and keypoints on image.
# Input is image: tensor([[[]]])
# Input is output from neural network model, i.e. {'boxes: tensor([[]]), 'scores': tensor([]), keypoints: tensor([[[]]])}
# Output is an annotated image
def draw_label_on_single_img(img, target, NN_iou_threshold = 0.1):
    # Transform tensor to image
    toPilImg = T.ToPILImage()
    
    # Convert tensor image to array
    img = torch.as_tensor(img.detach().cpu().numpy())
    img = np.array(toPilImg(img).convert('RGB'))
    
    # Perform nms
    if 'scores' in target:
        nms = torchvision.ops.nms(target['boxes'], target['scores'], iou_threshold = NN_iou_threshold)
        nms = nms.detach().numpy()
    else:
        nms = list(range(len(target['boxes'])))

    # Plot boxes and keypoints for each fish
    boxes = target['boxes'].detach().cpu().numpy()
    for i in nms:
        cv2.rectangle(img, 
            tuple(boxes[i][:2].astype(int)),
            tuple(boxes[i][2:].astype(int)), 
            (255,0,0), 5)
        for keypoint in range(3):
            color = (255,255,255)
            if keypoint == 0: color = (255,0,0) # ljaw
            if keypoint == 1: color = (0,255,0) # ujaw
            if keypoint == 2: color = (0,0,255) # eye
            cv2.circle(img, 
                        (int(target['keypoints'][i][keypoint][0]), int(target['keypoints'][i][keypoint][1])), 5,
                        color, 5)
    return img

# Draw bounding boxes and keypoints on image.
# Input is image: tensor([[[]]])
# Input is list of active trackers, i.e. [{last_bbox: [4], last_keypoints = [3], dists[n], first_frame: c, last_frame: c, box_number: c}, {...}, ...]
# Output is an annotated image
def draw_active_tracker(img, active_trackers):
    toPilImg = T.ToPILImage()
    img = torch.as_tensor(img.detach().cpu().numpy())
    img = np.array(toPilImg(img).convert('RGB'))
    for instance in active_trackers:
        cv2.rectangle(img, 
            tuple(instance['last_bbox'][:2].astype(int)),
            tuple(instance['last_bbox'][2:].astype(int)), 
            (255,0,0), 5)
        for keypoint in range(3):
            color = (255,255,255)
            if keypoint == 0: color = (255,0,0) # ljaw
            if keypoint == 1: color = (0,255,0) # ujaw
            if keypoint == 2: color = (0,0,255) # eye
            cv2.circle(img, 
                        (int(instance['last_keypoints'][keypoint][0]), int(instance['last_keypoints'][keypoint][1])), 5,
                        color, 5)
        cv2.putText(img, str(['Box nr. ', str(instance['box_count'])]), tuple(instance['last_bbox'][:2].astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 1, (209, 80, 0, 255), 3) 
    return img