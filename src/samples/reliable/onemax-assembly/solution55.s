    .file   "solution.c"
    .text
    .globl  _darwin
    .def    _darwin;        .scl    2;      .type   32;     .endef
_darwin:
LFB17:
    .cfi_startproc
    pushl   %ebp
    .cfi_def_cfa_offset 8
    .cfi_offset 5, -8
    movl    %esp, %ebp
    .cfi_def_cfa_register 5

    movl	$-22195, %eax
    movl	$11278, %ebx
    movl	$-14131, %ecx
    movl	$7280, %edx

    shr $233, %ecx
    shr $47, %ecx
    and %ecx, %edx
    jz n31
    jnc n25
    add %ecx, %edx
    sub %eax, %ecx
    jc n27
    shl $107, %ebx
    jmp n14
    jz n32
n14:
    jno n17
    or %ecx, %edx
    xor %ecx, %ecx
n17:
    xor %ecx, %ebx
    xor %edx, %edx
    or %ebx, %ebx
    jne n24
    shr $60, %eax
    or %eax, %ebx
    xor %edx, %edx
n24:
    add %ecx, %ecx
n25:
    jno n29
    ja n32
n27:
    je n33
    shl $130, %eax
n29:
    shl $153, %ecx
    add %eax, %ecx
n31:
    and %edx, %eax
n32:
    sub %ebx, %ecx
n33:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
